# Module 3.10: Dashboard Feature (PlantUML)
> Contains 2 class diagrams.

## 3.10.1 Overview Class Diagram - Dashboard Feature (`dashboard_overview`)

```plantuml
@startuml
title 3.10.1 Overview Class Diagram - Dashboard Feature
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class DashboardController {
  -dashboardService: DashboardService
  +getStats(startDate?: string, endDate?: string, facilityId?: string, user?: any): Promise<any>
}

class DashboardService {
  -prisma: PrismaService
  +getStats(startDateStr?: string, endDateStr?: string, facilityIdStr?: string, user?: any): Promise<any>
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
  +donations: PrismaDonationDelegate
  +blood_inventory: PrismaBloodInventoryDelegate
  +users: PrismaUserDelegate
  +facility_donation_schedules: PrismaScheduleDelegate
  +blood_requests: PrismaBloodRequestDelegate
  +blood_request_statuses: PrismaRequestStatusDelegate
  +blood_types: PrismaBloodTypeDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class donations {
  +donation_id: Int
  +donation_code: String
  +facility_id: Int
  +donor_user_id: Int
  +blood_type_id: Int
  +volume_ml: Int
  +donation_date: DateTime
  +status_code: String
  +created_at: DateTime
}

class blood_inventory {
  +inventory_id: Int
  +facility_id: Int
  +blood_type_id: Int
  +bag_code: String
  +volume_ml: Int
  +collection_date: DateTime
  +status_code: String
  +created_at: DateTime
}

class users {
  +user_id: Int
  +role_id: Int
  +full_name: String
  +email: String
  +is_active: Boolean
  +created_at: DateTime
}

class facility_donation_schedules {
  +schedule_id: Int
  +facility_id: Int
  +date: DateTime
  +status: String
  +max_donors: Int
  +current_donors: Int
}

class blood_requests {
  +request_id: Int
  +request_code: String
  +facility_id: Int
  +status_id: Int
  +is_emergency: Boolean
  +created_at: DateTime
}

class blood_request_statuses {
  +status_id: Int
  +status_code: String
  +status_name: String
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
  +abo: String
  +rh_factor: String
}

class medical_facilities {
  +facility_id: Int
  +facility_code: String
  +facility_name: String
  +is_primary: Boolean
  +is_active: Boolean
}

DashboardController --> DashboardService : Association
DashboardService --> PrismaService : Association
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- donations : Composition
PrismaService *-- blood_inventory : Composition
PrismaService *-- users : Composition
PrismaService *-- facility_donation_schedules : Composition
PrismaService *-- blood_requests : Composition
PrismaService *-- blood_request_statuses : Composition
PrismaService *-- blood_types : Composition
PrismaService *-- medical_facilities : Composition
medical_facilities "1" o-- "0..*" donations : Aggregation
medical_facilities "1" o-- "0..*" blood_inventory : Aggregation
medical_facilities "1" o-- "0..*" blood_requests : Aggregation
medical_facilities "1" o-- "0..*" facility_donation_schedules : Aggregation
blood_types "1" o-- "0..*" blood_inventory : Aggregation
blood_request_statuses "1" o-- "0..*" blood_requests : Aggregation
users "1" o-- "0..*" donations : Aggregation
@enduml
```

## 3.10.2.1 Class Diagram - Get Dashboard Statistics (`dashboard_stats`)

```plantuml
@startuml
title 3.10.2.1 Class Diagram - Get Dashboard Statistics
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class DashboardController {
  -dashboardService: DashboardService
  ...
  +getStats(startDate?: string, endDate?: string, facilityId?: string, user?: any): Promise<any>
  ...
}

class DashboardService {
  -prisma: PrismaService
  ...
  +getStats(startDateStr?: string, endDateStr?: string, facilityIdStr?: string, user?: any): Promise<any>
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
  +donations: PrismaDonationDelegate
  +blood_inventory: PrismaBloodInventoryDelegate
  +users: PrismaUserDelegate
  +facility_donation_schedules: PrismaScheduleDelegate
  +blood_requests: PrismaBloodRequestDelegate
  +blood_request_statuses: PrismaRequestStatusDelegate
  +blood_types: PrismaBloodTypeDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class donations {
  +donation_id: Int
  +facility_id: Int
  +donor_user_id: Int
  +volume_ml: Int
  +donation_date: DateTime
  +status_code: String
  +created_at: DateTime
}

class blood_inventory {
  +inventory_id: Int
  +facility_id: Int
  +blood_type_id: Int
  +volume_ml: Int
  +collection_date: DateTime
  +status_code: String
}

class users {
  +user_id: Int
  +role_id: Int
  +created_at: DateTime
}

class facility_donation_schedules {
  +schedule_id: Int
  +facility_id: Int
  +date: DateTime
  +status: String
}

class blood_requests {
  +request_id: Int
  +facility_id: Int
  +status_id: Int
  +is_emergency: Boolean
}

class blood_request_statuses {
  +status_id: Int
  +status_code: String
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
}

class medical_facilities {
  +facility_id: Int
  +facility_name: String
  +is_active: Boolean
}

DashboardController --> DashboardService : Association
DashboardService --> PrismaService : Association
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- donations : Composition
PrismaService *-- blood_inventory : Composition
PrismaService *-- users : Composition
PrismaService *-- facility_donation_schedules : Composition
PrismaService *-- blood_requests : Composition
PrismaService *-- blood_request_statuses : Composition
PrismaService *-- blood_types : Composition
PrismaService *-- medical_facilities : Composition
medical_facilities "1" o-- "0..*" donations : Aggregation
medical_facilities "1" o-- "0..*" blood_inventory : Aggregation
medical_facilities "1" o-- "0..*" blood_requests : Aggregation
medical_facilities "1" o-- "0..*" facility_donation_schedules : Aggregation
blood_types "1" o-- "0..*" blood_inventory : Aggregation
blood_request_statuses "1" o-- "0..*" blood_requests : Aggregation
users "1" o-- "0..*" donations : Aggregation
@enduml
```
