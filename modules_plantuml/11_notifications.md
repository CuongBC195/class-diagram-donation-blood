# Module 3.11: Notification Feature (PlantUML)
> Contains 3 class diagrams.

## 3.11.1 Overview Class Diagram - Notification Feature (`notifications_overview`)

```plantuml
@startuml
title 3.11.1 Overview Class Diagram - Notification Feature
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class NotificationsController {
  -notificationsService: NotificationsService
  +getMyNotifications(req: any, query: any): Promise<any>
  +getUnreadCount(req: any): Promise<any>
  +markAllAsRead(req: any): Promise<any>
  +createNotification(dto: CreateNotificationDto): Promise<any>
  +getNotifications(query: any): Promise<any>
  +deleteNotification(id: number): Promise<any>
  +markAsRead(id: number): Promise<any>
}

class CreateNotificationDto {
  +user_ids: number[]
  +title: string
  +message: string
  +notification_type: string
  +reference_type: string?
  +reference_id: number?
}

enum NotificationType {
  INFO
  SUCCESS
  WARNING
  SYSTEM
}

class NotificationsService {
  -prisma: PrismaService
  +createNotification(dto: CreateNotificationDto): Promise<any>
  +notifyAdmins(title: string, message: string, type: string, reference_type?: string, reference_id?: number): Promise<void>
  +getNotifications(query: any): Promise<any>
  +deleteNotification(id: number): Promise<any>
  +markAsRead(id: number): Promise<any>
  +getUnreadCount(userId: number): Promise<any>
  +markAllAsRead(userId: number): Promise<any>
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
  +notifications: PrismaNotificationDelegate
  +users: PrismaUserDelegate
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class notifications {
  +notification_id: Int
  +user_id: Int
  +title: String
  +message: String
  +notification_type: String
  +reference_type: String?
  +reference_id: Int?
  +is_read: Boolean
  +created_at: DateTime
  +read_at: DateTime?
  ...
}

class users {
  +user_id: Int
  +role_id: Int
  +full_name: String
  +email: String
  +is_active: Boolean
  ...
}

NotificationsController --> NotificationsService : Association
NotificationsController ..> CreateNotificationDto : Dependency
NotificationsService --> PrismaService : Association
NotificationsService ..> CreateNotificationDto : Dependency
NotificationsService ..> NotificationType : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- notifications : Composition
PrismaService *-- users : Composition
users "1" o-- "0..*" notifications : Aggregation
@enduml
```

## 3.11.2.1 Class Diagram - User Notification Operations (`notifications_user`)

```plantuml
@startuml
title 3.11.2.1 Class Diagram - User Notification Operations
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class NotificationsController {
  -notificationsService: NotificationsService
  +getMyNotifications(req: any, query: any): Promise<any>
  +getUnreadCount(req: any): Promise<any>
  +markAllAsRead(req: any): Promise<any>
  +markAsRead(id: number): Promise<any>
  ...
}

class NotificationsService {
  -prisma: PrismaService
  +getNotifications(query: any): Promise<any>
  +getUnreadCount(userId: number): Promise<any>
  +markAllAsRead(userId: number): Promise<any>
  +markAsRead(id: number): Promise<any>
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
  +notifications: PrismaNotificationDelegate
  +users: PrismaUserDelegate
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class notifications {
  +notification_id: Int
  +user_id: Int
  +title: String
  +message: String
  +notification_type: String
  +is_read: Boolean
  +created_at: DateTime
  +read_at: DateTime?
  ...
}

class users {
  +user_id: Int
  +full_name: String
  +email: String
  ...
}

NotificationsController --> NotificationsService : Association
NotificationsService --> PrismaService : Association
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- notifications : Composition
PrismaService *-- users : Composition
users "1" o-- "0..*" notifications : Aggregation
@enduml
```

## 3.11.2.2 Class Diagram - Admin Notification Management (`notifications_admin`)

```plantuml
@startuml
title 3.11.2.2 Class Diagram - Admin Notification Management
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class NotificationsController {
  -notificationsService: NotificationsService
  +createNotification(dto: CreateNotificationDto): Promise<any>
  +getNotifications(query: any): Promise<any>
  +deleteNotification(id: number): Promise<any>
  ...
}

class CreateNotificationDto {
  +user_ids: number[]
  +title: string
  +message: string
  +notification_type: string
  +reference_type: string?
  +reference_id: number?
}

enum NotificationType {
  INFO
  SUCCESS
  WARNING
  SYSTEM
}

class NotificationsService {
  -prisma: PrismaService
  +createNotification(dto: CreateNotificationDto): Promise<any>
  +notifyAdmins(title: string, message: string, type: string, reference_type?: string, reference_id?: number): Promise<void>
  +getNotifications(query: any): Promise<any>
  +deleteNotification(id: number): Promise<any>
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
  +notifications: PrismaNotificationDelegate
  +users: PrismaUserDelegate
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class notifications {
  +notification_id: Int
  +user_id: Int
  +title: String
  +message: String
  +notification_type: String
  +reference_type: String?
  +reference_id: Int?
  +is_read: Boolean
  +created_at: DateTime
  ...
}

class users {
  +user_id: Int
  +role_id: Int
  +full_name: String
  +email: String
  +is_active: Boolean
  ...
}

NotificationsController --> NotificationsService : Association
NotificationsController ..> CreateNotificationDto : Dependency
NotificationsService --> PrismaService : Association
NotificationsService ..> CreateNotificationDto : Dependency
NotificationsService ..> NotificationType : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- notifications : Composition
PrismaService *-- users : Composition
users "1" o-- "0..*" notifications : Aggregation
@enduml
```
