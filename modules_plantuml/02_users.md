# Module 3.2: User Profile and Account Administration Feature (PlantUML)
> Contains 6 class diagrams.

## 3.2.1 Overview Class Diagram - User Profile and Account Administration Feature (`users_overview`)

```plantuml
@startuml
title 3.2.1 Overview Class Diagram - User Profile and Account Administration Feature
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class UsersController {
  -usersService: UsersService
  +getProfile(req: any): Promise<any>
  +updateProfile(req: any, body: any): Promise<any>
  +uploadAvatar(req: any, file: Express.Multer.File): Promise<any>
  +requestChangePasswordOtp(req: any): Promise<any>
  +changePassword(req: any, dto: ChangePasswordVerifyDto): Promise<any>
  +getAllUsers(query: UserFilterDto): Promise<any>
  +exportExcel(query: UserFilterDto, res: Response): Promise<void>
  +downloadTemplate(res: Response): Promise<void>
  +importExcel(file: Express.Multer.File, req: any): Promise<any>
  +getUserById(id: number): Promise<any>
  +createUser(dto: CreateUserAdminDto): Promise<any>
  +updateUser(id: number, dto: UpdateUserAdminDto): Promise<any>
  +toggleLockUser(id: number): Promise<any>
}

class UsersService {
  -prisma: PrismaService
  -cloudinary: CloudinaryService
  -mailService: MailService
  -notificationsService: NotificationsService
  +getProfile(userId: number): Promise<any>
  +updateProfile(userId: number, data: any): Promise<any>
  +uploadAvatar(userId: number, file: Express.Multer.File): Promise<any>
  +sendChangePasswordOtp(userId: number): Promise<any>
  +changePassword(userId: number, dto: ChangePasswordVerifyDto): Promise<any>
  +getAllUsers(query: UserFilterDto): Promise<any>
  +exportExcel(query: UserFilterDto): Promise<Buffer>
  +getTemplate(): Promise<Buffer>
  +importExcel(buffer: Buffer, staffId: number): Promise<any>
  +getUserById(id: number): Promise<any>
  +createUserAdmin(dto: CreateUserAdminDto): Promise<any>
  +updateUserAdmin(id: number, dto: UpdateUserAdminDto): Promise<any>
  +toggleLockUser(id: number): Promise<any>
}

class UserFilterDto {
  +role_id: number?
  +is_active: boolean?
  +page: number?
  +limit: number?
  +search: string?
  +sortBy: string?
  +sortOrder: string?
}

class ChangePasswordVerifyDto {
  +otp_code: string
  +new_password: string
}

class DonorProfileInputDto {
  +blood_type_id: number?
  +weight_kg: number?
  +height_cm: number?
  +first_donation_date: Date?
  +total_donations: number?
  +last_donation_date: Date?
  +next_eligible_date: Date?
  +health_notes: string?
  +emergency_contact_name: string?
  +emergency_contact_phone: string?
  +is_active: boolean?
}

class CreateUserAdminDto {
  +email: string
  +password: string?
  +username: string?
  +full_name: string
  +phone: string?
  +date_of_birth: Date?
  +gender: string?
  +identity_card: string?
  +address: string?
  +province_id: number?
  +ward_id: number?
  +blood_type_id: number?
  +facility_id: number?
  +role_id: number
  +donor_profile: DonorProfileInputDto?
}

class UpdateUserAdminDto {
  +password: string?
  +full_name: string?
  +username: string?
  +phone: string?
  +email: string?
  +date_of_birth: Date?
  +gender: string?
  +identity_card: string?
  +address: string?
  +province_id: number?
  +ward_id: number?
  +blood_type_id: number?
  +facility_id: number?
  +role_id: number?
  +is_active: boolean?
  +donor_profile: DonorProfileInputDto?
}

class CloudinaryService {
  +uploadFile(file: Express.Multer.File): Promise<any>
  ...
}

class MailService {
  -logger: Logger
  -mailerService: MailerService
  +sendChangePasswordEmail(email: string, otpCode: string, name: string): Promise<void>
  ...
}

class NotificationsService {
  -prisma: PrismaService
  +createNotification(dto: CreateNotificationDto): Promise<any>
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
  +users: PrismaUserDelegate
  +roles: PrismaRoleDelegate
  +blood_types: PrismaBloodTypeDelegate
  +provinces: PrismaProvinceDelegate
  +wards: PrismaWardDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  +donor_profiles: PrismaDonorProfileDelegate
  +otp_types: PrismaOtpTypeDelegate
  +user_otps: PrismaUserOtpDelegate
  +notifications: PrismaNotificationDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class users {
  +user_id: Int
  +role_id: Int
  +facility_id: Int?
  +blood_type_id: Int?
  +province_id: Int?
  +ward_id: Int?
  +email: String
  +username: String?
  +password_hash: String
  +full_name: String
  +phone: String?
  +date_of_birth: DateTime?
  +gender: String?
  +avatar_url: String?
  +identity_card: String?
  +address: String?
  +is_active: Boolean
  +role: roles
  +blood_type: blood_types?
  +province: provinces?
  +ward: wards?
  +facility: medical_facilities?
  +donor_profile: donor_profiles?
  ...
}

class roles {
  +role_id: Int
  +role_code: String
  +role_name: String
  ...
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
  +abo: String
  +rh_factor: String
  ...
}

class provinces {
  +province_id: Int
  +province_code: String?
  +province_name: String
  ...
}

class wards {
  +ward_id: Int
  +province_id: Int
  +ward_name: String
  ...
}

class medical_facilities {
  +facility_id: Int
  +facility_name: String
  ...
}

class donor_profiles {
  +donor_profile_id: Int
  +user_id: Int
  +blood_type_id: Int
  +total_donations: Int
  ...
}

class otp_types {
  +otp_type_id: Int
  +otp_type_code: String
  +expiry_minutes: Int
  ...
}

class user_otps {
  +otp_id: BigInt
  +user_id: Int?
  +otp_type_id: Int
  +destination: String
  +otp_hash: String
  +expires_at: DateTime
  ...
}

class notifications {
  +notification_id: Int
  +user_id: Int
  +title: String
  +message: String
  ...
}

UsersController --> UsersService : Association
UsersController ..> UserFilterDto : Dependency
UsersController ..> ChangePasswordVerifyDto : Dependency
UsersController ..> CreateUserAdminDto : Dependency
UsersController ..> UpdateUserAdminDto : Dependency
UsersService --> PrismaService : Association
UsersService --> CloudinaryService : Association
UsersService --> MailService : Association
UsersService --> NotificationsService : Association
UsersService ..> UserFilterDto : Dependency
UsersService ..> ChangePasswordVerifyDto : Dependency
UsersService ..> CreateUserAdminDto : Dependency
UsersService ..> UpdateUserAdminDto : Dependency
CreateUserAdminDto ..> DonorProfileInputDto : Dependency
UpdateUserAdminDto ..> DonorProfileInputDto : Dependency
NotificationsService --> PrismaService : Association
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- users : Composition
PrismaService *-- roles : Composition
PrismaService *-- blood_types : Composition
PrismaService *-- provinces : Composition
PrismaService *-- wards : Composition
PrismaService *-- medical_facilities : Composition
PrismaService *-- donor_profiles : Composition
PrismaService *-- otp_types : Composition
PrismaService *-- user_otps : Composition
PrismaService *-- notifications : Composition
roles "1" o-- "0..*" users : Aggregation
blood_types "0..1" o-- "0..*" users : Aggregation
provinces "0..1" o-- "0..*" users : Aggregation
wards "0..1" o-- "0..*" users : Aggregation
medical_facilities "0..1" o-- "0..*" users : Aggregation
users "1" o-- "0..1" donor_profiles : Aggregation
users "0..1" o-- "0..*" user_otps : Aggregation
otp_types "1" *-- "0..*" user_otps : Composition
users "1" o-- "0..*" notifications : Aggregation
@enduml
```

## 3.2.2.1 Class Diagram - View and Update Profile (`users_profile`)

```plantuml
@startuml
title 3.2.2.1 Class Diagram - View and Update Profile
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class UsersController {
  -usersService: UsersService
  ...
  +getProfile(req: any): Promise<any>
  +updateProfile(req: any, body: any): Promise<any>
  ...
}

class UsersService {
  -prisma: PrismaService
  ...
  +getProfile(userId: number): Promise<any>
  +updateProfile(userId: number, data: any): Promise<any>
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
  +users: PrismaUserDelegate
  +roles: PrismaRoleDelegate
  +blood_types: PrismaBloodTypeDelegate
  +provinces: PrismaProvinceDelegate
  +wards: PrismaWardDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class users {
  +user_id: Int
  +role_id: Int
  +facility_id: Int?
  +blood_type_id: Int?
  +province_id: Int?
  +ward_id: Int?
  +email: String
  +full_name: String
  +phone: String?
  +date_of_birth: DateTime?
  +gender: String?
  +avatar_url: String?
  +address: String?
  +role: roles
  +blood_type: blood_types?
  +province: provinces?
  +ward: wards?
  +facility: medical_facilities?
  ...
}

class roles {
  +role_id: Int
  +role_code: String
  +role_name: String
  ...
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
  +abo: String
  +rh_factor: String
  ...
}

class provinces {
  +province_id: Int
  +province_code: String?
  +province_name: String
  ...
}

class wards {
  +ward_id: Int
  +province_id: Int
  +ward_name: String
  ...
}

class medical_facilities {
  +facility_id: Int
  +facility_name: String
  ...
}

UsersController --> UsersService : Association
UsersService --> PrismaService : Association
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- users : Composition
PrismaService *-- roles : Composition
PrismaService *-- blood_types : Composition
PrismaService *-- provinces : Composition
PrismaService *-- wards : Composition
PrismaService *-- medical_facilities : Composition
roles "1" o-- "0..*" users : Aggregation
blood_types "0..1" o-- "0..*" users : Aggregation
provinces "0..1" o-- "0..*" users : Aggregation
wards "0..1" o-- "0..*" users : Aggregation
medical_facilities "0..1" o-- "0..*" users : Aggregation
@enduml
```

## 3.2.2.2 Class Diagram - Upload Profile Avatar (`users_avatar`)

```plantuml
@startuml
title 3.2.2.2 Class Diagram - Upload Profile Avatar
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class UsersController {
  -usersService: UsersService
  ...
  +uploadAvatar(req: any, file: Express.Multer.File): Promise<any>
  ...
}

class UsersService {
  -prisma: PrismaService
  -cloudinary: CloudinaryService
  ...
  +uploadAvatar(userId: number, file: Express.Multer.File): Promise<any>
  ...
}

class CloudinaryService {
  +uploadFile(file: Express.Multer.File): Promise<any>
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
  +users: PrismaUserDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class users {
  +user_id: Int
  +avatar_url: String?
  ...
}

UsersController --> UsersService : Association
UsersService --> PrismaService : Association
UsersService --> CloudinaryService : Association
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- users : Composition
@enduml
```

## 3.2.2.3 Class Diagram - Change Password with OTP (`users_change_password`)

```plantuml
@startuml
title 3.2.2.3 Class Diagram - Change Password with OTP
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class UsersController {
  -usersService: UsersService
  ...
  +requestChangePasswordOtp(req: any): Promise<any>
  +changePassword(req: any, dto: ChangePasswordVerifyDto): Promise<any>
  ...
}

class ChangePasswordVerifyDto {
  +otp_code: string
  +new_password: string
}

class CreateNotificationDto {
  +user_ids: number[]
  +title: string
  +message: string
  +notification_type: string
}

enum OtpTypeCode {
  CHANGE_PASSWORD
  ...
}

enum DestinationType {
  EMAIL
  ...
}

enum NotificationType {
  SUCCESS
  ...
}

class UsersService {
  -prisma: PrismaService
  -mailService: MailService
  -notificationsService: NotificationsService
  ...
  +sendChangePasswordOtp(userId: number): Promise<any>
  +changePassword(userId: number, dto: ChangePasswordVerifyDto): Promise<any>
  ...
}

class Bcrypt <<utility>> {
  +hash(data: string, saltOrRounds: any): Promise<string>
  +compare(data: string, encrypted: string): Promise<boolean>
  +genSalt(rounds: number): Promise<string>
  ...
}

class MailService {
  -mailerService: MailerService
  ...
  +sendChangePasswordEmail(email: string, otpCode: string, name: string): Promise<void>
  ...
}

class MailerService {
  +sendMail(options: object): Promise<any>
  ...
}

class NotificationsService {
  -prisma: PrismaService
  ...
  +createNotification(dto: CreateNotificationDto): Promise<any>
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
  +users: PrismaUserDelegate
  +otp_types: PrismaOtpTypeDelegate
  +user_otps: PrismaUserOtpDelegate
  +notifications: PrismaNotificationDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class users {
  +user_id: Int
  +email: String
  +full_name: String
  +password_hash: String
  ...
}

class otp_types {
  +otp_type_id: Int
  +otp_type_code: String
  +expiry_minutes: Int
  ...
}

class user_otps {
  +otp_id: BigInt
  +user_id: Int?
  +otp_type_id: Int
  +destination: String
  +destination_type: String
  +otp_hash: String
  +is_verified: Boolean
  +attempt_count: Int
  +expires_at: DateTime
  +verified_at: DateTime?
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

UsersController --> UsersService : Association
UsersController ..> ChangePasswordVerifyDto : Dependency
UsersService --> PrismaService : Association
UsersService --> MailService : Association
UsersService --> NotificationsService : Association
UsersService ..> ChangePasswordVerifyDto : Dependency
UsersService ..> OtpTypeCode : Dependency
UsersService ..> DestinationType : Dependency
UsersService ..> NotificationType : Dependency
UsersService ..> CreateNotificationDto : Dependency
UsersService ..> Bcrypt : Dependency
MailService --> MailerService : Association
NotificationsService --> PrismaService : Association
NotificationsService ..> CreateNotificationDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- users : Composition
PrismaService *-- otp_types : Composition
PrismaService *-- user_otps : Composition
PrismaService *-- notifications : Composition
users "0..1" o-- "0..*" user_otps : Aggregation
otp_types "1" *-- "0..*" user_otps : Composition
users "1" o-- "0..*" notifications : Aggregation
@enduml
```

## 3.2.2.4 Class Diagram - Admin Manage Users (`users_admin_manage`)

```plantuml
@startuml
title 3.2.2.4 Class Diagram - Admin Manage Users
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class UsersController {
  -usersService: UsersService
  ...
  +getAllUsers(query: UserFilterDto): Promise<any>
  +getUserById(id: number): Promise<any>
  +createUser(dto: CreateUserAdminDto): Promise<any>
  +updateUser(id: number, dto: UpdateUserAdminDto): Promise<any>
  +toggleLockUser(id: number): Promise<any>
  ...
}

class UserFilterDto {
  +role_id: number?
  +is_active: boolean?
  +page: number?
  +limit: number?
  +search: string?
  +sortBy: string?
  +sortOrder: string?
}

class DonorProfileInputDto {
  +blood_type_id: number?
  +weight_kg: number?
  +height_cm: number?
  +first_donation_date: Date?
  +total_donations: number?
  +last_donation_date: Date?
  +next_eligible_date: Date?
  +health_notes: string?
  +emergency_contact_name: string?
  +emergency_contact_phone: string?
  +is_active: boolean?
}

class CreateUserAdminDto {
  +email: string
  +password: string?
  +username: string?
  +full_name: string
  +phone: string?
  +date_of_birth: Date?
  +gender: string?
  +identity_card: string?
  +address: string?
  +province_id: number?
  +ward_id: number?
  +blood_type_id: number?
  +facility_id: number?
  +role_id: number
  +donor_profile: DonorProfileInputDto?
}

class UpdateUserAdminDto {
  +password: string?
  +full_name: string?
  +username: string?
  +phone: string?
  +email: string?
  +date_of_birth: Date?
  +gender: string?
  +identity_card: string?
  +address: string?
  +province_id: number?
  +ward_id: number?
  +blood_type_id: number?
  +facility_id: number?
  +role_id: number?
  +is_active: boolean?
  +donor_profile: DonorProfileInputDto?
}

class UsersService {
  -prisma: PrismaService
  ...
  +getAllUsers(query: UserFilterDto): Promise<any>
  +getUserById(id: number): Promise<any>
  +createUserAdmin(dto: CreateUserAdminDto): Promise<any>
  +updateUserAdmin(id: number, dto: UpdateUserAdminDto): Promise<any>
  +toggleLockUser(id: number): Promise<any>
  ...
}

class Bcrypt <<utility>> {
  +hash(data: string, saltOrRounds: any): Promise<string>
  +genSalt(rounds: number): Promise<string>
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
  +users: PrismaUserDelegate
  +roles: PrismaRoleDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  +donor_profiles: PrismaDonorProfileDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class users {
  +user_id: Int
  +role_id: Int
  +facility_id: Int?
  +blood_type_id: Int?
  +province_id: Int?
  +ward_id: Int?
  +email: String
  +username: String?
  +password_hash: String
  +full_name: String
  +phone: String?
  +date_of_birth: DateTime?
  +gender: String?
  +identity_card: String?
  +address: String?
  +is_active: Boolean
  +role: roles
  +facility: medical_facilities?
  +donor_profile: donor_profiles?
  ...
}

class roles {
  +role_id: Int
  +role_code: String
  +role_name: String
  ...
}

class medical_facilities {
  +facility_id: Int
  +facility_name: String
  ...
}

class donor_profiles {
  +donor_profile_id: Int
  +user_id: Int
  +blood_type_id: Int
  +total_donations: Int
  ...
}

UsersController --> UsersService : Association
UsersController ..> UserFilterDto : Dependency
UsersController ..> CreateUserAdminDto : Dependency
UsersController ..> UpdateUserAdminDto : Dependency
UsersService --> PrismaService : Association
UsersService ..> UserFilterDto : Dependency
UsersService ..> CreateUserAdminDto : Dependency
UsersService ..> UpdateUserAdminDto : Dependency
UsersService ..> Bcrypt : Dependency
CreateUserAdminDto ..> DonorProfileInputDto : Dependency
UpdateUserAdminDto ..> DonorProfileInputDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- users : Composition
PrismaService *-- roles : Composition
PrismaService *-- medical_facilities : Composition
PrismaService *-- donor_profiles : Composition
roles "1" o-- "0..*" users : Aggregation
medical_facilities "0..1" o-- "0..*" users : Aggregation
users "1" o-- "0..1" donor_profiles : Aggregation
@enduml
```

## 3.2.2.5 Class Diagram - Import and Export Users Excel (`users_excel`)

```plantuml
@startuml
title 3.2.2.5 Class Diagram - Import and Export Users Excel
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class UsersController {
  -usersService: UsersService
  ...
  +exportExcel(query: UserFilterDto, res: Response): Promise<void>
  +downloadTemplate(res: Response): Promise<void>
  +importExcel(file: Express.Multer.File, req: any): Promise<any>
  ...
}

class UserFilterDto {
  +role_id: number?
  +is_active: boolean?
  +page: number?
  +limit: number?
  +search: string?
  +sortBy: string?
  +sortOrder: string?
}

class UsersService {
  -prisma: PrismaService
  ...
  +exportExcel(query: any): Promise<Buffer>
  +getTemplate(): Promise<Buffer>
  +importExcel(buffer: Buffer, staffId: number): Promise<any>
  ...
}

class ExcelUtil <<utility>> {
  +generateExcel(data: any[], sheetName: string): Buffer
  +generateTemplate(headers: string[], sheetName: string): Buffer
  +parseExcel(buffer: Buffer): any[]
}

class Bcrypt <<utility>> {
  +hash(data: string, saltOrRounds: any): Promise<string>
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
  +users: PrismaUserDelegate
  +roles: PrismaRoleDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class users {
  +user_id: Int
  +role_id: Int
  +facility_id: Int?
  +email: String
  +full_name: String
  +password_hash: String
  +phone: String?
  +identity_card: String?
  +date_of_birth: DateTime?
  +gender: String?
  +is_active: Boolean
  +role: roles
  +facility: medical_facilities?
  ...
}

class roles {
  +role_id: Int
  +role_code: String
  +role_name: String
  ...
}

class medical_facilities {
  +facility_id: Int
  +facility_name: String
  ...
}

UsersController --> UsersService : Association
UsersController ..> UserFilterDto : Dependency
UsersService --> PrismaService : Association
UsersService ..> UserFilterDto : Dependency
UsersService ..> ExcelUtil : Dependency
UsersService ..> Bcrypt : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- users : Composition
PrismaService *-- roles : Composition
PrismaService *-- medical_facilities : Composition
roles "1" o-- "0..*" users : Aggregation
medical_facilities "0..1" o-- "0..*" users : Aggregation
@enduml
```
