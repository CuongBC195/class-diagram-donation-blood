# Module 3.12: System Settings Feature (Mermaid)
> Contains 2 class diagrams.

## 3.12.1 Overview Class Diagram - System Settings Feature (`system_settings_overview`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class SystemSettingsController {
  -systemSettingsService: SystemSettingsService
  +getSettings(query: any): Promise~any~
  +upsertSetting(dto: UpsertSettingDto): Promise~any~
  +deleteSetting(id: number): Promise~any~
}

class UpsertSettingDto {
  +setting_key: string
  +setting_value: string
  +description: string?
}

class SystemSettingsService {
  -prisma: PrismaService
  +getSettings(query: any): Promise~any~
  +upsertSetting(dto: UpsertSettingDto): Promise~any~
  +deleteSetting(id: number): Promise~any~
}

class OnModuleInit {
  <<interface>>
  +onModuleInit(): Promise~void~
}

class OnModuleDestroy {
  <<interface>>
  +onModuleDestroy(): Promise~void~
}

class PrismaClient {
  +$connect(): Promise~void~
  +$disconnect(): Promise~void~
  ...
}

class PrismaService {
  +system_settings: PrismaSystemSettingDelegate
  ...
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class system_settings {
  +setting_id: Int
  +setting_key: String
  +setting_value: String
  +description: String?
  +updated_at: DateTime
}

SystemSettingsController --> SystemSettingsService : Association
SystemSettingsController ..> UpsertSettingDto : Dependency

SystemSettingsService --> PrismaService : Association
SystemSettingsService ..> UpsertSettingDto : Dependency

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- system_settings : Composition
```

## 3.12.2.1 Class Diagram - View and Update System Settings (`system_settings_crud`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class SystemSettingsController {
  -systemSettingsService: SystemSettingsService
  +getSettings(query: any): Promise~any~
  +upsertSetting(dto: UpsertSettingDto): Promise~any~
  +deleteSetting(id: number): Promise~any~
}

class UpsertSettingDto {
  +setting_key: string
  +setting_value: string
  +description: string?
}

class SystemSettingsService {
  -prisma: PrismaService
  +getSettings(query: any): Promise~any~
  +upsertSetting(dto: UpsertSettingDto): Promise~any~
  +deleteSetting(id: number): Promise~any~
}

class OnModuleInit {
  <<interface>>
  +onModuleInit(): Promise~void~
}

class OnModuleDestroy {
  <<interface>>
  +onModuleDestroy(): Promise~void~
}

class PrismaClient {
  +$connect(): Promise~void~
  +$disconnect(): Promise~void~
  ...
}

class PrismaService {
  +system_settings: PrismaSystemSettingDelegate
  ...
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class system_settings {
  +setting_id: Int
  +setting_key: String
  +setting_value: String
  +description: String?
  +updated_at: DateTime
}

SystemSettingsController --> SystemSettingsService : Association
SystemSettingsController ..> UpsertSettingDto : Dependency

SystemSettingsService --> PrismaService : Association
SystemSettingsService ..> UpsertSettingDto : Dependency

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- system_settings : Composition
```
