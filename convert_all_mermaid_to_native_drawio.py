#!/usr/bin/env python3
"""Batch convert all 61 Mermaid class diagrams (.mmd) into native Draw.io XML workbooks
using Draw.io's official headless engine, ensuring 100% beautiful graph layout,
zero overlapping boxes, perfectly routed arrows, and full multi-tab integration.
"""

from __future__ import annotations
import copy
import subprocess
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from master_class_definitions import MODULE_SPECS

ROOT = Path(__file__).resolve().parent
MMD_DIR = ROOT / "full_detailed_design" / "master_class"
DRAWIO_BIN = "/Applications/draw.io.app/Contents/MacOS/draw.io"

DESTINATIONS = [
    ROOT.parent / "class-diagram-new",
    Path("/Users/bcc/FPT/BloodLink/class-diagram-new"),
]

TMP_DIR = Path("/tmp/drawio_mermaid_batch")
TMP_DIR.mkdir(parents=True, exist_ok=True)

def fix_drawio_styles(drawio_file: Path):
    import re
    tree = ET.parse(drawio_file)
    root = tree.getroot()
    changed = False
    for uo in root.iter("UserObject"):
        cell = uo.find("mxCell")
        if cell is not None and "swimlane" in cell.attrib.get("style", ""):
            style = cell.attrib["style"]
            m_sz = re.search(r"startSize=(\d+)", style)
            if m_sz:
                sz = int(m_sz.group(1))
                if sz > 48:
                    new_style = re.sub(r"marginTop=\d+", f"marginTop={sz}", style)
                    if new_style != style:
                        cell.attrib["style"] = new_style
                        changed = True

    # Replace purple edge label background with white (#ffffff)
    for cell in root.iter("mxCell"):
        if cell.attrib.get("edge") == "1":
            style = cell.attrib.get("style", "")
            if "labelBackgroundColor=" in style:
                new_style = re.sub(r"labelBackgroundColor=[^;]+", "labelBackgroundColor=#ffffff", style)
                if new_style != style:
                    cell.attrib["style"] = new_style
                    changed = True

    for uo in root.iter("UserObject"):
        style = uo.attrib.get("mermaidBaseStyle", "")
        if "labelBackgroundColor=" in style:
            new_style = re.sub(r"labelBackgroundColor=[^;]+", "labelBackgroundColor=#ffffff", style)
            if new_style != style:
                uo.attrib["mermaidBaseStyle"] = new_style
                changed = True

    if changed:
        tree.write(drawio_file, encoding="utf-8", xml_declaration=True)

def convert_single_mmd(key: str) -> Path:
    mmd_path = MMD_DIR / f"{key}.mmd"
    out_drawio = TMP_DIR / f"{key}.drawio"
    
    # Cache check with mtime
    if out_drawio.exists() and out_drawio.stat().st_size > 500:
        if out_drawio.stat().st_mtime >= mmd_path.stat().st_mtime:
            return out_drawio
        
    cmd = [DRAWIO_BIN, "-x", "-f", "xml", "-o", str(out_drawio), str(mmd_path)]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    fix_drawio_styles(out_drawio)
    return out_drawio

def main():
    print("🚀 Bắt đầu chuyển đổi 61 sơ đồ Mermaid sang Draw.io Native Engine...")
    t0 = time.time()
    
    all_keys = []
    for mod in MODULE_SPECS:
        for key, tab_name, fig_title in mod["actions"]:
            all_keys.append(key)
            
    total = len(all_keys)
    print(f"Tổng số sơ đồ cần chuyển đổi: {total}")
    
    # Sequential conversion to guarantee stability on Electron
    for idx, key in enumerate(all_keys, 1):
        t_start = time.time()
        convert_single_mmd(key)
        print(f"  [{idx:02d}/{total}] Converted: {key}.mmd in {time.time()-t_start:.2f}s")

    print(f"\n✅ Đã chuyển đổi xong toàn bộ {total} sơ đồ trong {time.time()-t0:.2f}s!")
    print("🔨 Đang lắp ráp vào các file multi-tab Draw.io...")

    # Cache parsed diagrams
    diagram_nodes = {}
    for key in all_keys:
        f = TMP_DIR / f"{key}.drawio"
        tree = ET.parse(f)
        diag = tree.find("diagram")
        if diag is None:
            raise ValueError(f"No <diagram> tag found in {f}")
        diagram_nodes[key] = diag

    # Grand master
    grand_mx = ET.Element("mxfile", {"host": "Electron", "version": "32.4.1"})
    
    for mod in MODULE_SPECS:
        mod_id = mod["id"]
        mod_num = mod["num"]
        out_file_name = mod["out_file"]
        
        # Module master
        mod_mx = ET.Element("mxfile", {"host": "Electron", "version": "32.4.1"})
        
        for key, tab_name, fig_title in mod["actions"]:
            diag_node = diagram_nodes[key]
            
            # Module tab
            tab_node = copy.deepcopy(diag_node)
            tab_node.attrib["id"] = f"{mod_id}_{key}"
            tab_node.attrib["name"] = f"{mod_num} {tab_name}"
            mod_mx.append(tab_node)
            
            # Grand tab
            g_tab = copy.deepcopy(diag_node)
            g_tab.attrib["id"] = f"{mod_id}_{key}"
            g_tab.attrib["name"] = f"{mod_num} {tab_name}"
            grand_mx.append(g_tab)
            
        # Write module file
        ET.indent(mod_mx, space="  ")
        xml_str = ET.tostring(mod_mx, encoding="unicode")
        for dst in DESTINATIONS:
            p = dst / out_file_name
            p.write_text(xml_str, encoding="utf-8")
        print(f"  [Module Workbook] {out_file_name} ({len(mod['actions'])} tabs)")

    # Write Grand Master
    ET.indent(grand_mx, space="  ")
    grand_xml = ET.tostring(grand_mx, encoding="unicode")
    for dst in DESTINATIONS:
        gp = dst / "all_features_class_diagrams.drawio"
        gp.write_text(grand_xml, encoding="utf-8")
    print(f"\n🎉 [GRAND MASTER] all_features_class_diagrams.drawio ({total} tabs) đã được tạo thành công!")

if __name__ == "__main__":
    main()
