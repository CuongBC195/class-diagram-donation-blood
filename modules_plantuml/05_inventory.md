# Module 3.5: Blood Inventory Feature (PlantUML)
> Contains 6 class diagrams.

## 3.5.1 Overview Class Diagram - Blood Inventory Feature (`inventory_overview`)

```plantuml
@startuml
title 3.5.1 Overview Class Diagram - Blood Inventory Feature
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class InventoryController {
  -inventoryService: InventoryService
  +receiveBlood(req: any, dto: ReceiveBloodDto): Promise<any>
  +updateBlood(req: any, inventoryId: number, dto: Partial<ReceiveBloodDto>): Promise<any>
  +discardBlood(req: any, inventoryId: number, dto: DiscardBloodDto): Promise<any>
  +getStats(req: any): Promise<any>
  +getInventoryList(query: any, req: any): Promise<any>
  +exportExcel(query: any, res: Response, req: any): Promise<void>
  +downloadTemplate(res: Response): Promise<void>
  +importExcel(file: Express.Multer.File, req: any): Promise<any>
}

class ReceiveBloodDto {
  +facility_id: number
  +blood_type_id: number
  +component_id: number
  +bag_code: string
  +volume_ml: number
  +collection_date: Date
  +expiry_date: Date
  +source_donation_id: number?
  +notes: string?
}

class UpdateBloodDto {
  +facility_id: number?
  +blood_type_id: number?
  +component_id: number?
  +bag_code: string?
  +volume_ml: number?
  +collection_date: Date?
  +expiry_date: Date?
  +source_donation_id: number?
  +notes: string?
}

class ExcelUtil <<utility>> {
  +generateExcel(data: any[], sheetName: string): Buffer
  +generateTemplate(headers: string[], sheetName: string): Buffer
  +parseExcel(buffer: Buffer): any[]
}

class DiscardBloodDto {
  +reason: string
}

class InventoryService {
  -prisma: PrismaService
  +receiveBlood(dto: any, user: any): Promise<any>
  +updateBlood(inventoryId: number, dto: any, user: any): Promise<any>
  +discardBlood(inventoryId: number, user: any, reason: string): Promise<any>
  +getInventoryStats(user: any): Promise<any>
  +getInventoryList(query: any, user: any): Promise<any>
  +exportExcel(query: any, user: any): Promise<Buffer>
  +getTemplate(): Promise<Buffer>
  +importExcel(buffer: Buffer, staffId: number): Promise<any>
}

interface OnModuleInit {
  +onModuleInit(): Promise<void>
}

interface OnModuleDestroy {
  +onModuleDestroy(): Promise<void>
}

class PrismaClient {
  +$connect(): Promise<void>
  +$disconnect(): Promise<void>
  +$transaction(callback: any): Promise<any>
  ...
}

class PrismaService {
  +blood_inventory: PrismaBloodInventoryDelegate
  +inventory_transactions: PrismaInventoryTransactionDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  +blood_types: PrismaBloodTypeDelegate
  +blood_components: PrismaBloodComponentDelegate
  +users: PrismaUserDelegate
  +donations: PrismaDonationDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class blood_inventory {
  +inventory_id: Int
  +bag_code: String
  +facility_id: Int
  +blood_type_id: Int
  +component_id: Int
  +volume_ml: Int
  +collection_date: DateTime
  +expiry_date: DateTime
  +status_code: String
  +source_donation_id: Int?
  +notes: String?
  ...
}

class inventory_transactions {
  +transaction_id: Int
  +inventory_id: Int
  +transaction_type: String
  +quantity: Int
  +reference_type: String?
  +reference_id: Int?
  +performed_by: Int?
  +notes: String?
  +created_at: DateTime
  ...
}

class medical_facilities {
  +facility_id: Int
  +facility_code: String
  +facility_name: String
  +phone: String?
  +address: String
  ...
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
  +abo: String
  +rh_factor: String
  ...
}

class blood_components {
  +component_id: Int
  +component_code: String
  +component_name: String
  ...
}

class users {
  +user_id: Int
  +full_name: String
  +email: String
  ...
}

class donations {
  +donation_id: Int
  +donation_code: String
  ...
}

InventoryController --> InventoryService : Association
InventoryController ..> ReceiveBloodDto : Dependency
InventoryController ..> UpdateBloodDto : Dependency
InventoryController ..> DiscardBloodDto : Dependency
InventoryService --> PrismaService : Association
InventoryService ..> ReceiveBloodDto : Dependency
InventoryService ..> UpdateBloodDto : Dependency
InventoryService ..> ExcelUtil : Dependency
InventoryService ..> DiscardBloodDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- blood_inventory : Composition
PrismaService *-- inventory_transactions : Composition
PrismaService *-- medical_facilities : Composition
PrismaService *-- blood_types : Composition
PrismaService *-- blood_components : Composition
PrismaService *-- users : Composition
PrismaService *-- donations : Composition
medical_facilities "1" o-- "0..*" blood_inventory : Aggregation
blood_types "1" o-- "0..*" blood_inventory : Aggregation
blood_components "1" o-- "0..*" blood_inventory : Aggregation
donations "0..1" o-- "0..*" blood_inventory : Aggregation
blood_inventory "1" o-- "0..*" inventory_transactions : Aggregation
users "1" o-- "0..*" inventory_transactions : Aggregation
@enduml
```

## 3.5.2.1 Class Diagram - View Inventory List and Statistics (`inventory_list_stats`)

```plantuml
@startuml
title 3.5.2.1 Class Diagram - View Inventory List and Statistics
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class InventoryController {
  -inventoryService: InventoryService
  ...
  +getInventoryList(query: any, req: any): Promise<any>
  +getStats(req: any): Promise<any>
  ...
}

class InventoryService {
  -prisma: PrismaService
  ...
  +getInventoryList(query: any, user: any): Promise<any>
  +getInventoryStats(user: any): Promise<any>
  ...
}

interface OnModuleInit {
  +onModuleInit(): Promise<void>
}

interface OnModuleDestroy {
  +onModuleDestroy(): Promise<void>
}

class PrismaClient {
  +$connect(): Promise<void>
  +$disconnect(): Promise<void>
  ...
}

class PrismaService {
  +blood_inventory: PrismaBloodInventoryDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  +blood_types: PrismaBloodTypeDelegate
  +blood_components: PrismaBloodComponentDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class blood_inventory {
  +inventory_id: Int
  +bag_code: String
  +facility_id: Int
  +blood_type_id: Int
  +component_id: Int
  +volume_ml: Int
  +collection_date: DateTime
  +expiry_date: DateTime
  +status_code: String
  ...
}

class medical_facilities {
  +facility_id: Int
  +facility_name: String
  ...
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
  ...
}

class blood_components {
  +component_id: Int
  +component_name: String
  ...
}

InventoryController --> InventoryService : Association
InventoryService --> PrismaService : Association
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- blood_inventory : Composition
PrismaService *-- medical_facilities : Composition
PrismaService *-- blood_types : Composition
PrismaService *-- blood_components : Composition
medical_facilities "1" o-- "0..*" blood_inventory : Aggregation
blood_types "1" o-- "0..*" blood_inventory : Aggregation
blood_components "1" o-- "0..*" blood_inventory : Aggregation
@enduml
```

## 3.5.2.2 Class Diagram - Receive Blood Unit (`inventory_receive`)

```plantuml
@startuml
title 3.5.2.2 Class Diagram - Receive Blood Unit
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class InventoryController {
  -inventoryService: InventoryService
  ...
  +receiveBlood(req: any, dto: ReceiveBloodDto): Promise<any>
  ...
}

class ReceiveBloodDto {
  +facility_id: number
  +blood_type_id: number
  +component_id: number
  +bag_code: string
  +volume_ml: number
  +collection_date: Date
  +expiry_date: Date
  +source_donation_id: number?
  +notes: string?
}

class InventoryService {
  -prisma: PrismaService
  ...
  +receiveBlood(dto: any, user: any): Promise<any>
  ...
}

interface OnModuleInit {
  +onModuleInit(): Promise<void>
}

interface OnModuleDestroy {
  +onModuleDestroy(): Promise<void>
}

class PrismaClient {
  +$connect(): Promise<void>
  +$disconnect(): Promise<void>
  +$transaction(callback: any): Promise<any>
  ...
}

class PrismaService {
  +blood_inventory: PrismaBloodInventoryDelegate
  +inventory_transactions: PrismaInventoryTransactionDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class blood_inventory {
  +inventory_id: Int
  +bag_code: String
  +facility_id: Int
  +blood_type_id: Int
  +component_id: Int
  +volume_ml: Int
  +collection_date: DateTime
  +expiry_date: DateTime
  +status_code: String
  +source_donation_id: Int?
  ...
}

class inventory_transactions {
  +transaction_id: Int
  +inventory_id: Int
  +transaction_type: String
  +quantity: Int
  +reference_type: String?
  +reference_id: Int?
  +performed_by: Int?
  ...
}

InventoryController --> InventoryService : Association
InventoryController ..> ReceiveBloodDto : Dependency
InventoryService --> PrismaService : Association
InventoryService ..> ReceiveBloodDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- blood_inventory : Composition
PrismaService *-- inventory_transactions : Composition
blood_inventory "1" o-- "0..*" inventory_transactions : Aggregation
@enduml
```

## 3.5.2.3 Class Diagram - Update Blood Unit (`inventory_update`)

```plantuml
@startuml
title 3.5.2.3 Class Diagram - Update Blood Unit
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class InventoryController {
  -inventoryService: InventoryService
  ...
  +updateBlood(req: any, inventoryId: number, dto: UpdateBloodDto): Promise<any>
  ...
}

class UpdateBloodDto {
  +facility_id: number?
  +blood_type_id: number?
  +component_id: number?
  +bag_code: string?
  +volume_ml: number?
  +collection_date: Date?
  +expiry_date: Date?
  +source_donation_id: number?
  +notes: string?
}

class InventoryService {
  -prisma: PrismaService
  ...
  +updateBlood(inventoryId: number, dto: any, user: any): Promise<any>
  ...
}

interface OnModuleInit {
  +onModuleInit(): Promise<void>
}

interface OnModuleDestroy {
  +onModuleDestroy(): Promise<void>
}

class PrismaClient {
  +$connect(): Promise<void>
  +$disconnect(): Promise<void>
  ...
}

class PrismaService {
  +blood_inventory: PrismaBloodInventoryDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class blood_inventory {
  +inventory_id: Int
  +bag_code: String
  +volume_ml: Int
  +collection_date: DateTime
  +expiry_date: DateTime
  +status_code: String
  +notes: String?
  ...
}

InventoryController --> InventoryService : Association
InventoryController ..> UpdateBloodDto : Dependency
InventoryService --> PrismaService : Association
InventoryService ..> UpdateBloodDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- blood_inventory : Composition
@enduml
```

## 3.5.2.4 Class Diagram - Discard Blood Unit (`inventory_discard`)

```plantuml
@startuml
title 3.5.2.4 Class Diagram - Discard Blood Unit
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class InventoryController {
  -inventoryService: InventoryService
  ...
  +discardBlood(req: any, inventoryId: number, dto: DiscardBloodDto): Promise<any>
  ...
}

class DiscardBloodDto {
  +reason: string
}

class InventoryService {
  -prisma: PrismaService
  ...
  +discardBlood(inventoryId: number, user: any, reason: string): Promise<any>
  ...
}

interface OnModuleInit {
  +onModuleInit(): Promise<void>
}

interface OnModuleDestroy {
  +onModuleDestroy(): Promise<void>
}

class PrismaClient {
  +$connect(): Promise<void>
  +$disconnect(): Promise<void>
  +$transaction(callback: any): Promise<any>
  ...
}

class PrismaService {
  +blood_inventory: PrismaBloodInventoryDelegate
  +inventory_transactions: PrismaInventoryTransactionDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class blood_inventory {
  +inventory_id: Int
  +bag_code: String
  +status_code: String
  ...
}

class inventory_transactions {
  +transaction_id: Int
  +inventory_id: Int
  +transaction_type: String
  +quantity: Int
  +reference_type: String?
  +performed_by: Int?
  +notes: String?
  ...
}

InventoryController --> InventoryService : Association
InventoryController ..> DiscardBloodDto : Dependency
InventoryService --> PrismaService : Association
InventoryService ..> DiscardBloodDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- blood_inventory : Composition
PrismaService *-- inventory_transactions : Composition
blood_inventory "1" o-- "0..*" inventory_transactions : Aggregation
@enduml
```

## 3.5.2.5 Class Diagram - Import and Export Inventory Excel (`inventory_excel`)

```plantuml
@startuml
title 3.5.2.5 Class Diagram - Import and Export Inventory Excel
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class InventoryController {
  -inventoryService: InventoryService
  ...
  +exportExcel(query: any, res: Response, req: any): Promise<void>
  +downloadTemplate(res: Response): Promise<void>
  +importExcel(file: Express.Multer.File, req: any): Promise<any>
  ...
}

class InventoryService {
  -prisma: PrismaService
  ...
  +exportExcel(query: any, user: any): Promise<Buffer>
  +getTemplate(): Promise<Buffer>
  +importExcel(buffer: Buffer, staffId: number): Promise<any>
  ...
}

class ExcelUtil <<utility>> {
  +generateExcel(data: any[], sheetName?: string): Buffer
  +generateTemplate(headers: string[], sheetName?: string): Buffer
  +parseExcel(buffer: Buffer): any[]
}

interface OnModuleInit {
  +onModuleInit(): Promise<void>
}

interface OnModuleDestroy {
  +onModuleDestroy(): Promise<void>
}

class PrismaClient {
  +$connect(): Promise<void>
  +$disconnect(): Promise<void>
  ...
}

class PrismaService {
  +blood_inventory: PrismaBloodInventoryDelegate
  +inventory_transactions: PrismaInventoryTransactionDelegate
  +users: PrismaUserDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class blood_inventory {
  +inventory_id: Int
  +bag_code: String
  +facility_id: Int
  +blood_type_id: Int
  +component_id: Int
  +volume_ml: Int
  +collection_date: DateTime
  +expiry_date: DateTime
  +status_code: String
  ...
}

class inventory_transactions {
  +transaction_id: Int
  +inventory_id: Int
  +transaction_type: String
  +quantity: Int
  +performed_by: Int?
  ...
}

class users {
  +user_id: Int
  +full_name: String
  ...
}

InventoryController --> InventoryService : Association
InventoryService --> PrismaService : Association
InventoryService ..> ExcelUtil : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- blood_inventory : Composition
PrismaService *-- inventory_transactions : Composition
PrismaService *-- users : Composition
blood_inventory "1" o-- "0..*" inventory_transactions : Aggregation
users "1" o-- "0..*" inventory_transactions : Aggregation
@enduml
```
