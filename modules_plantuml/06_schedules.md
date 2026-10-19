# Module 3.6: Donation Schedule Administration Feature (PlantUML)
> Contains 3 class diagrams.

## 3.6.1 Overview Class Diagram - Donation Schedule Administration Feature (`schedules_overview`)

```plantuml
@startuml
title 3.6.1 Overview Class Diagram - Donation Schedule Administration Feature
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class SchedulesController {
  -schedulesService: SchedulesService
  +getAllSchedules(query: ScheduleFilterDto, user: any): Promise<any>
  +getScheduleById(id: number, user: any): Promise<any>
  +createSchedule(dto: CreateScheduleDto, user: any): Promise<any>
  +updateSchedule(id: number, dto: UpdateScheduleDto, user: any): Promise<any>
  +deleteSchedule(id: number, user: any): Promise<any>
  +getScheduleDonors(id: number, query: any, user: any): Promise<any>
  +updateDonorStatus(id: number, slotId: number, status: string, user: any): Promise<any>
  +exportScheduleDonors(id: number, res: Response, user: any): Promise<any>
}

class CreateScheduleDto {
  +facility_id: number
  +date: string
  +start_time: string
  +end_time: string
  +max_donors: number?
  +status: string?
  +terms_html: string?
}

class UpdateScheduleDto {
  +facility_id: number?
  +date: string?
  +start_time: string?
  +end_time: string?
  +max_donors: number?
  +status: string?
  +terms_html: string?
}

class ScheduleFilterDto {
  +facility_id: number?
  +date: string?
  +status: string?
  +page: number?
  +limit: number?
}

class SchedulesService {
  -logger: Logger
  -prisma: PrismaService
  -notificationsService: NotificationsService
  +onModuleInit(): Promise<void>
  +handleCronClosePastSchedules(): Promise<void>
  +getAllSchedules(query: ScheduleFilterDto, user: any): Promise<any>
  +getScheduleById(id: number, user: any): Promise<any>
  +createSchedule(dto: CreateScheduleDto, user: any): Promise<any>
  +updateSchedule(id: number, dto: UpdateScheduleDto, user: any): Promise<any>
  +deleteSchedule(id: number, user: any): Promise<any>
  +getScheduleDonors(scheduleId: number, query: any, user: any): Promise<any>
  +updateDonorStatus(scheduleId: number, slotId: number, status: string, user: any): Promise<any>
  +exportScheduleDonors(scheduleId: number, user: any): Promise<object>
}

class NotificationsService {
  -prisma: PrismaService
  +createNotification(dto: CreateNotificationDto): Promise<any>
  ...
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
  ...
}

class ExcelUtil <<utility>> {
  +generateExcel(data: any[], sheetName: string): Buffer
  +generateTemplate(headers: string[], sheetName: string): Buffer
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
  +facility_donation_schedules: PrismaDonationScheduleDelegate
  +donor_availability_slots: PrismaAvailabilitySlotDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  +users: PrismaUserDelegate
  +notifications: PrismaNotificationDelegate
  +blood_types: PrismaBloodTypeDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class facility_donation_schedules {
  +schedule_id: Int
  +facility_id: Int
  +date: DateTime
  +start_time: DateTime
  +end_time: DateTime
  +max_donors: Int
  +current_donors: Int
  +status: String
  +terms_html: String?
  ...
}

class donor_availability_slots {
  +slot_id: Int
  +user_id: Int
  +schedule_id: Int?
  +status: String
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

class users {
  +user_id: Int
  +full_name: String
  +email: String
  +phone: String?
  +gender: String?
  +blood_type_id: Int?
  ...
}

class notifications {
  +notification_id: Int
  +user_id: Int
  +title: String
  +message: String
  +notification_type: String
  ...
}

SchedulesController --> SchedulesService : Association
SchedulesController ..> ScheduleFilterDto : Dependency
SchedulesController ..> CreateScheduleDto : Dependency
SchedulesController ..> UpdateScheduleDto : Dependency
SchedulesService --> PrismaService : Association
SchedulesService --> NotificationsService : Association
SchedulesService ..|> OnModuleInit : Implements
SchedulesService ..> ScheduleFilterDto : Dependency
SchedulesService ..> CreateScheduleDto : Dependency
SchedulesService ..> UpdateScheduleDto : Dependency
SchedulesService ..> ExcelUtil : Dependency
NotificationsService --> PrismaService : Association
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- facility_donation_schedules : Composition
PrismaService *-- donor_availability_slots : Composition
PrismaService *-- medical_facilities : Composition
PrismaService *-- users : Composition
PrismaService *-- notifications : Composition
PrismaService *-- blood_types : Composition
medical_facilities "1" o-- "0..*" facility_donation_schedules : Aggregation
facility_donation_schedules "1" o-- "0..*" donor_availability_slots : Aggregation
users "1" o-- "0..*" donor_availability_slots : Aggregation
users "1" o-- "0..*" notifications : Aggregation
blood_types "0..1" o-- "0..*" users : Aggregation
@enduml
```

## 3.6.2.1 Class Diagram - View and Manage Donation Schedules (`schedules_crud`)

```plantuml
@startuml
title 3.6.2.1 Class Diagram - View and Manage Donation Schedules
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class SchedulesController {
  -schedulesService: SchedulesService
  ...
  +getAllSchedules(query: ScheduleFilterDto, user: any): Promise<any>
  +getScheduleById(id: number, user: any): Promise<any>
  +createSchedule(dto: CreateScheduleDto, user: any): Promise<any>
  +updateSchedule(id: number, dto: UpdateScheduleDto, user: any): Promise<any>
  +deleteSchedule(id: number, user: any): Promise<any>
  ...
}

class CreateScheduleDto {
  +facility_id: number
  +date: string
  +start_time: string
  +end_time: string
  +max_donors: number?
  +status: string?
  +terms_html: string?
}

class UpdateScheduleDto {
  +facility_id: number?
  +date: string?
  +start_time: string?
  +end_time: string?
  +max_donors: number?
  +status: string?
  +terms_html: string?
}

class ScheduleFilterDto {
  +facility_id: number?
  +date: string?
  +status: string?
  +page: number?
  +limit: number?
}

class SchedulesService {
  -logger: Logger
  -prisma: PrismaService
  ...
  +onModuleInit(): Promise<void>
  +handleCronClosePastSchedules(): Promise<void>
  +getAllSchedules(query: ScheduleFilterDto, user: any): Promise<any>
  +getScheduleById(id: number, user: any): Promise<any>
  +createSchedule(dto: CreateScheduleDto, user: any): Promise<any>
  +updateSchedule(id: number, dto: UpdateScheduleDto, user: any): Promise<any>
  +deleteSchedule(id: number, user: any): Promise<any>
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
  +facility_donation_schedules: PrismaDonationScheduleDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  +donor_availability_slots: PrismaAvailabilitySlotDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class facility_donation_schedules {
  +schedule_id: Int
  +facility_id: Int
  +date: DateTime
  +start_time: DateTime
  +end_time: DateTime
  +max_donors: Int
  +current_donors: Int
  +status: String
  +terms_html: String?
  ...
}

class medical_facilities {
  +facility_id: Int
  +facility_name: String
  +address: String
  ...
}

class donor_availability_slots {
  +slot_id: Int
  +schedule_id: Int?
  +status: String
  ...
}

SchedulesController --> SchedulesService : Association
SchedulesController ..> ScheduleFilterDto : Dependency
SchedulesController ..> CreateScheduleDto : Dependency
SchedulesController ..> UpdateScheduleDto : Dependency
SchedulesService --> PrismaService : Association
SchedulesService ..|> OnModuleInit : Implements
SchedulesService ..> ScheduleFilterDto : Dependency
SchedulesService ..> CreateScheduleDto : Dependency
SchedulesService ..> UpdateScheduleDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- facility_donation_schedules : Composition
PrismaService *-- medical_facilities : Composition
PrismaService *-- donor_availability_slots : Composition
medical_facilities "1" o-- "0..*" facility_donation_schedules : Aggregation
facility_donation_schedules "1" o-- "0..*" donor_availability_slots : Aggregation
@enduml
```

## 3.6.2.2 Class Diagram - Track Schedule Donors and Excel Export (`schedules_donors_excel`)

```plantuml
@startuml
title 3.6.2.2 Class Diagram - Track Schedule Donors and Excel Export
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class SchedulesController {
  -schedulesService: SchedulesService
  ...
  +getScheduleDonors(id: number, query: any, user: any): Promise<any>
  +updateDonorStatus(id: number, slotId: number, status: string, user: any): Promise<any>
  +exportScheduleDonors(id: number, res: Response, user: any): Promise<any>
  ...
}

class CreateNotificationDto {
  +user_ids: number[]
  +title: string
  +message: string
  +notification_type: NotificationType
  +reference_type: string?
  +reference_id: number?
}

enum NotificationType {
  INFO
}

class SchedulesService {
  -logger: Logger
  -prisma: PrismaService
  -notificationsService: NotificationsService
  ...
  +getScheduleDonors(scheduleId: number, query: any, user: any): Promise<any>
  +updateDonorStatus(scheduleId: number, slotId: number, status: string, user: any): Promise<any>
  +exportScheduleDonors(scheduleId: number, user: any): Promise<object>
  ...
}

class NotificationsService {
  -prisma: PrismaService
  +createNotification(dto: CreateNotificationDto): Promise<any>
  ...
}

class ExcelUtil <<utility>> {
  +generateExcel(data: any[], sheetName?: string): Buffer
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
  +facility_donation_schedules: PrismaDonationScheduleDelegate
  +donor_availability_slots: PrismaAvailabilitySlotDelegate
  +users: PrismaUserDelegate
  +blood_types: PrismaBloodTypeDelegate
  +notifications: PrismaNotificationDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class facility_donation_schedules {
  +schedule_id: Int
  +facility_id: Int
  +date: DateTime
  ...
}

class donor_availability_slots {
  +slot_id: Int
  +user_id: Int
  +schedule_id: Int?
  +status: String
  +created_at: DateTime
  ...
}

class users {
  +user_id: Int
  +full_name: String
  +email: String
  +phone: String?
  +gender: String?
  +blood_type_id: Int?
  ...
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
  ...
}

class notifications {
  +notification_id: Int
  +user_id: Int
  +title: String
  +message: String
  ...
}

SchedulesController --> SchedulesService : Association
SchedulesService --> PrismaService : Association
SchedulesService --> NotificationsService : Association
SchedulesService ..> ExcelUtil : Dependency
NotificationsService --> PrismaService : Association
NotificationsService ..> CreateNotificationDto : Dependency
CreateNotificationDto ..> NotificationType : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- facility_donation_schedules : Composition
PrismaService *-- donor_availability_slots : Composition
PrismaService *-- users : Composition
PrismaService *-- blood_types : Composition
PrismaService *-- notifications : Composition
facility_donation_schedules "1" o-- "0..*" donor_availability_slots : Aggregation
users "1" o-- "0..*" donor_availability_slots : Aggregation
blood_types "0..1" o-- "0..*" users : Aggregation
users "1" o-- "0..*" notifications : Aggregation
@enduml
```
