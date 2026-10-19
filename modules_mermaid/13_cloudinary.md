# Module 3.13: File Upload Feature (Mermaid)
> Contains 2 class diagrams.

## 3.13.1 Overview Class Diagram - File Upload Feature (`cloudinary_overview`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class CloudinaryController {
  -cloudinaryService: CloudinaryService
  +uploadImage(file: Express.Multer.File): Promise~any~
}

class CloudinaryService {
  +uploadFile(file: Express.Multer.File): Promise~any~
}

class CloudinaryProvider {
  <<utility>>
  +provide: string
  +useFactory(): any
}

class CloudinarySDK {
  <<utility>>
  +config(options: object): any
  +upload_stream(callback: any): any
}

CloudinaryController --> CloudinaryService : Association
CloudinaryService ..> CloudinaryProvider : Dependency
CloudinaryService ..> CloudinarySDK : Dependency
CloudinaryProvider ..> CloudinarySDK : Dependency
```

## 3.13.2.1 Class Diagram - Upload Image (`cloudinary_upload`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class CloudinaryController {
  -cloudinaryService: CloudinaryService
  ...
  +uploadImage(file: Express.Multer.File): Promise~any~
  ...
}

class CloudinaryService {
  +uploadFile(file: Express.Multer.File): Promise~any~
}

class CloudinaryProvider {
  <<utility>>
  +provide: string
  +useFactory(): any
}

class CloudinarySDK {
  <<utility>>
  +config(options: object): any
  +upload_stream(callback: any): any
}

CloudinaryController --> CloudinaryService : Association
CloudinaryService ..> CloudinaryProvider : Dependency
CloudinaryService ..> CloudinarySDK : Dependency
CloudinaryProvider ..> CloudinarySDK : Dependency
```
