# Module 3.1: Auth Feature (Mermaid)
> Contains 8 class diagrams.

## 3.1.1 Overview Class Diagram - Auth Feature (`auth_overview`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class AuthController {
  -authService: AuthService
  +register(dto: RegisterDto): Promise~any~
  +verifyOtp(dto: OtpDto): Promise~any~
  +resendOtp(dto: ResendOtpDto): Promise~any~
  +login(dto: LoginDto): Promise~any~
  +refreshToken(dto: RefreshTokenDto): Promise~any~
  +forgotPassword(dto: ForgotPasswordDto): Promise~any~
  +resetPassword(dto: ResetPasswordDto): Promise~any~
}

class AuthService {
  -prisma: PrismaService
  -jwtService: JwtService
  -mailService: MailService
  -notificationsService: NotificationsService
  +register(dto: RegisterDto): Promise~any~
  +verifyOtp(dto: OtpDto): Promise~any~
  +resendOtp(dto: ResendOtpDto): Promise~any~
  +login(dto: LoginDto): Promise~any~
  +refreshToken(refreshToken: string): Promise~any~
  +forgotPassword(dto: ForgotPasswordDto): Promise~any~
  +resetPassword(dto: ResetPasswordDto): Promise~any~
}

class RegisterDto {
  +email: string
  +username: string?
  +password: string
  +full_name: string
}

class LoginDto {
  +identifier: string
  +password: string
}

class OtpDto {
  +email: string
  +otp_code: string
}

class ResendOtpDto {
  +email: string
}

class RefreshTokenDto {
  +refresh_token: string
}

class ForgotPasswordDto {
  +email: string
}

class ResetPasswordDto {
  +email: string
  +otp_code: string
  +new_password: string
}

class JwtService {
  +sign(payload: object): string
  +verify(token: string): any
  ...
}

class MailService {
  -logger: Logger
  -mailerService: MailerService
  +sendVerificationEmail(email: string, otpCode: string, name: string): Promise~void~
  +sendForgotPasswordEmail(email: string, otpCode: string): Promise~void~
  ...
}

class MailerService {
  +sendMail(options: object): Promise~any~
  ...
}

class NotificationsService {
  -prisma: PrismaService
  +createNotification(dto: CreateNotificationDto): Promise~any~
  +notifyAdmins(title: string, message: string, type: string, reference_type?: string, reference_id?: number): Promise~void~
  ...
}

class JwtStrategy {
  -prisma: PrismaService
  +validate(payload: any): Promise~any~
}

class PassportStrategy {

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
  +$transaction(callback: any): Promise~any~
  ...
}

class PrismaService {
  +users: PrismaUserDelegate
  +roles: PrismaRoleDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  +otp_types: PrismaOtpTypeDelegate
  +user_otps: PrismaUserOtpDelegate
  +notifications: PrismaNotificationDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class users {
  +user_id: Int
  +role_id: Int
  +facility_id: Int?
  +email: String
  +username: String?
  +password_hash: String
  +full_name: String
  +avatar_url: String?
  +refresh_token: String?
  +last_login_at: DateTime?
  +is_email_verified: Boolean
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

class otp_types {
  +otp_type_id: Int
  +otp_type_code: String
  +expiry_minutes: Int
  +max_attempts: Int
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
  +is_read: Boolean
  +created_at: DateTime
  ...
}

AuthController --> AuthService : Association

AuthController ..> RegisterDto : Dependency
AuthController ..> LoginDto : Dependency
AuthController ..> OtpDto : Dependency
AuthController ..> ResendOtpDto : Dependency
AuthController ..> RefreshTokenDto : Dependency
AuthController ..> ForgotPasswordDto : Dependency
AuthController ..> ResetPasswordDto : Dependency

AuthService ..> RegisterDto : Dependency
AuthService ..> LoginDto : Dependency
AuthService ..> OtpDto : Dependency
AuthService ..> ResendOtpDto : Dependency
AuthService ..> ForgotPasswordDto : Dependency
AuthService ..> ResetPasswordDto : Dependency

AuthService --> PrismaService : Association
AuthService --> JwtService : Association
AuthService --> MailService : Association
AuthService --> NotificationsService : Association

JwtStrategy --|> PassportStrategy : Inheritance
JwtStrategy --> PrismaService : Association

MailService --> MailerService : Association
NotificationsService --> PrismaService : Association

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- users : Composition
PrismaService *-- roles : Composition
PrismaService *-- medical_facilities : Composition
PrismaService *-- otp_types : Composition
PrismaService *-- user_otps : Composition
PrismaService *-- notifications : Composition

roles "1" o-- "0..*" users : Aggregation
medical_facilities "0..1" o-- "0..*" users : Aggregation
users "0..1" o-- "0..*" user_otps : Aggregation
otp_types "1" o-- "0..*" user_otps : Aggregation
users "1" o-- "0..*" notifications : Aggregation
```

## 3.1.2.1 Class Diagram - Register (`auth_register`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class AuthController {
  -authService: AuthService
  +register(dto: RegisterDto): Promise~any~
  ...
}

class RegisterDto {
  +email: string
  +username: string?
  +password: string
  +full_name: string
}

class RoleCode {
  <<enumeration>>
  MEMBER
}

class OtpTypeCode {
  <<enumeration>>
  REGISTER_VERIFY
}

class DestinationType {
  <<enumeration>>
  EMAIL
}

class AuthService {
  -prisma: PrismaService
  -mailService: MailService
  +register(dto: RegisterDto): Promise~any~
  ...
}

class Bcrypt {
  <<utility>>
  +hash(data: string, saltOrRounds: any): Promise~string~
  +genSalt(rounds: number): Promise~string~
}

class MailService {
  -mailerService: MailerService
  +sendVerificationEmail(email: string, otpCode: string, name: string): Promise~void~
  ...
}

class MailerService {
  +sendMail(options: object): Promise~any~
  ...
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
  +$transaction(callback: any): Promise~any~
  ...
}

class PrismaService {
  +users: PrismaUserDelegate
  +roles: PrismaRoleDelegate
  +otp_types: PrismaOtpTypeDelegate
  +user_otps: PrismaUserOtpDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class users {
  +user_id: Int
  +role_id: Int
  +email: String
  +username: String?
  +password_hash: String
  +full_name: String
  +is_email_verified: Boolean
  +is_active: Boolean
  ...
}

class roles {
  +role_id: Int
  +role_code: String
  ...
}

class otp_types {
  +otp_type_id: Int
  +otp_type_code: String
  ...
}

class user_otps {
  +otp_id: BigInt
  +user_id: Int?
  +otp_type_id: Int
  +destination: String
  +destination_type: String
  +otp_hash: String
  +expires_at: DateTime
  ...
}

AuthController --> AuthService : Association
AuthController ..> RegisterDto : Dependency

AuthService --> PrismaService : Association
AuthService --> MailService : Association
AuthService ..> RegisterDto : Dependency
AuthService ..> RoleCode : Dependency
AuthService ..> OtpTypeCode : Dependency
AuthService ..> DestinationType : Dependency
AuthService ..> Bcrypt : Dependency

MailService --> MailerService : Association

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- users : Composition
PrismaService *-- roles : Composition
PrismaService *-- otp_types : Composition
PrismaService *-- user_otps : Composition

roles "1" o-- "0..*" users : Aggregation
users "0..1" o-- "0..*" user_otps : Aggregation
otp_types "1" o-- "0..*" user_otps : Aggregation
```

## 3.1.2.2 Class Diagram - Verify OTP (`auth_verify_otp`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class AuthController {
  -authService: AuthService
  +verifyOtp(dto: OtpDto): Promise~any~
  ...
}

class OtpDto {
  +email: string
  +otp_code: string
}

class CreateNotificationDto {
  +user_ids: number[]
  +title: string
  +message: string
  +notification_type: string
  +reference_type: string?
  +reference_id: number?
}

class OtpTypeCode {
  <<enumeration>>
  REGISTER_VERIFY
}

class NotificationType {
  <<enumeration>>
  INFO
}

class AuthService {
  -prisma: PrismaService
  -notificationsService: NotificationsService
  +verifyOtp(dto: OtpDto): Promise~any~
  ...
}

class Bcrypt {
  <<utility>>
  +compare(data: string, encrypted: string): Promise~boolean~
}

class NotificationsService {
  -prisma: PrismaService
  +createNotification(dto: CreateNotificationDto): Promise~any~
  +notifyAdmins(title: string, message: string, type: string, reference_type?: string, reference_id?: number): Promise~void~
  ...
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
  +$transaction(callback: any): Promise~any~
  ...
}

class PrismaService {
  +users: PrismaUserDelegate
  +otp_types: PrismaOtpTypeDelegate
  +user_otps: PrismaUserOtpDelegate
  +notifications: PrismaNotificationDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class users {
  +user_id: Int
  +email: String
  +full_name: String
  +is_email_verified: Boolean
  +is_active: Boolean
  ...
}

class otp_types {
  +otp_type_id: Int
  +otp_type_code: String
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

AuthController --> AuthService : Association
AuthController ..> OtpDto : Dependency

AuthService --> PrismaService : Association
AuthService --> NotificationsService : Association
AuthService ..> OtpDto : Dependency
AuthService ..> OtpTypeCode : Dependency
AuthService ..> NotificationType : Dependency
AuthService ..> CreateNotificationDto : Dependency
AuthService ..> Bcrypt : Dependency

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
otp_types "1" o-- "0..*" user_otps : Aggregation
users "1" o-- "0..*" notifications : Aggregation
```

## 3.1.2.3 Class Diagram - Resend OTP (`auth_resend_otp`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class AuthController {
  -authService: AuthService
  +resendOtp(dto: ResendOtpDto): Promise~any~
  ...
}

class ResendOtpDto {
  +email: string
}

class OtpTypeCode {
  <<enumeration>>
  REGISTER_VERIFY
}

class DestinationType {
  <<enumeration>>
  EMAIL
}

class AuthService {
  -prisma: PrismaService
  -mailService: MailService
  +resendOtp(dto: ResendOtpDto): Promise~any~
  ...
}

class Bcrypt {
  <<utility>>
  +hash(data: string, saltOrRounds: any): Promise~string~
}

class MailService {
  -mailerService: MailerService
  +sendVerificationEmail(email: string, otpCode: string, name: string): Promise~void~
  ...
}

class MailerService {
  +sendMail(options: object): Promise~any~
  ...
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
  +users: PrismaUserDelegate
  +otp_types: PrismaOtpTypeDelegate
  +user_otps: PrismaUserOtpDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class users {
  +user_id: Int
  +email: String
  +full_name: String
  +is_email_verified: Boolean
  ...
}

class otp_types {
  +otp_type_id: Int
  +otp_type_code: String
  ...
}

class user_otps {
  +otp_id: BigInt
  +user_id: Int?
  +otp_type_id: Int
  +destination: String
  +destination_type: String
  +otp_hash: String
  +expires_at: DateTime
  ...
}

AuthController --> AuthService : Association
AuthController ..> ResendOtpDto : Dependency

AuthService --> PrismaService : Association
AuthService --> MailService : Association
AuthService ..> ResendOtpDto : Dependency
AuthService ..> OtpTypeCode : Dependency
AuthService ..> DestinationType : Dependency
AuthService ..> Bcrypt : Dependency

MailService --> MailerService : Association

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- users : Composition
PrismaService *-- otp_types : Composition
PrismaService *-- user_otps : Composition

users "0..1" o-- "0..*" user_otps : Aggregation
otp_types "1" o-- "0..*" user_otps : Aggregation
```

## 3.1.2.4 Class Diagram - Login (`auth_login`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class AuthController {
  -authService: AuthService
  +login(dto: LoginDto): Promise~any~
  ...
}

class LoginDto {
  +identifier: string
  +password: string
}

class AuthService {
  -prisma: PrismaService
  -jwtService: JwtService
  +login(dto: LoginDto): Promise~any~
  ...
}

class JwtService {
  +sign(payload: object): string
  ...
}

class Bcrypt {
  <<utility>>
  +compare(data: string, encrypted: string): Promise~boolean~
}

class Crypto {
  <<utility>>
  +randomBytes(size: number): Buffer
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
  +users: PrismaUserDelegate
  +roles: PrismaRoleDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class users {
  +user_id: Int
  +role_id: Int
  +facility_id: Int?
  +email: String
  +username: String?
  +password_hash: String
  +full_name: String
  +avatar_url: String?
  +refresh_token: String?
  +last_login_at: DateTime?
  +is_email_verified: Boolean
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

AuthController --> AuthService : Association
AuthController ..> LoginDto : Dependency

AuthService --> PrismaService : Association
AuthService --> JwtService : Association
AuthService ..> LoginDto : Dependency
AuthService ..> Bcrypt : Dependency
AuthService ..> Crypto : Dependency

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- users : Composition
PrismaService *-- roles : Composition
PrismaService *-- medical_facilities : Composition

roles "1" o-- "0..*" users : Aggregation
medical_facilities "0..1" o-- "0..*" users : Aggregation
```

## 3.1.2.5 Class Diagram - Refresh Token (`auth_refresh_token`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class AuthController {
  -authService: AuthService
  +refreshToken(dto: RefreshTokenDto): Promise~any~
  ...
}

class RefreshTokenDto {
  +refresh_token: string
}

class AuthService {
  -prisma: PrismaService
  -jwtService: JwtService
  +refreshToken(refreshToken: string): Promise~any~
  ...
}

class JwtService {
  +sign(payload: object): string
  ...
}

class Crypto {
  <<utility>>
  +randomBytes(size: number): Buffer
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
  +users: PrismaUserDelegate
  +roles: PrismaRoleDelegate
  +medical_facilities: PrismaMedicalFacilityDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class users {
  +user_id: Int
  +facility_id: Int?
  +email: String
  +full_name: String
  +avatar_url: String?
  +refresh_token: String?
  +role: roles
  +facility: medical_facilities?
  ...
}

class roles {
  +role_id: Int
  +role_code: String
  ...
}

class medical_facilities {
  +facility_id: Int
  +facility_name: String
  ...
}

AuthController --> AuthService : Association
AuthController ..> RefreshTokenDto : Dependency

AuthService --> PrismaService : Association
AuthService --> JwtService : Association
AuthService ..> Crypto : Dependency

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- users : Composition
PrismaService *-- roles : Composition
PrismaService *-- medical_facilities : Composition

roles "1" o-- "0..*" users : Aggregation
medical_facilities "0..1" o-- "0..*" users : Aggregation
```

## 3.1.2.6 Class Diagram - Forgot Password (`auth_forgot_password`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class AuthController {
  -authService: AuthService
  +forgotPassword(dto: ForgotPasswordDto): Promise~any~
  ...
}

class ForgotPasswordDto {
  +email: string
}

class OtpTypeCode {
  <<enumeration>>
  RESET_PASSWORD
}

class DestinationType {
  <<enumeration>>
  EMAIL
}

class AuthService {
  -prisma: PrismaService
  -mailService: MailService
  +forgotPassword(dto: ForgotPasswordDto): Promise~any~
  ...
}

class Bcrypt {
  <<utility>>
  +hash(data: string, saltOrRounds: any): Promise~string~
}

class MailService {
  -mailerService: MailerService
  +sendForgotPasswordEmail(email: string, otpCode: string): Promise~void~
  ...
}

class MailerService {
  +sendMail(options: object): Promise~any~
  ...
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
  +$transaction(callback: any): Promise~any~
  ...
}

class PrismaService {
  +users: PrismaUserDelegate
  +otp_types: PrismaOtpTypeDelegate
  +user_otps: PrismaUserOtpDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class users {
  +user_id: Int
  +email: String
  +full_name: String
  ...
}

class otp_types {
  +otp_type_id: Int
  +otp_type_code: String
  ...
}

class user_otps {
  +otp_id: BigInt
  +user_id: Int?
  +otp_type_id: Int
  +destination: String
  +destination_type: String
  +otp_hash: String
  +expires_at: DateTime
  ...
}

AuthController --> AuthService : Association
AuthController ..> ForgotPasswordDto : Dependency

AuthService --> PrismaService : Association
AuthService --> MailService : Association
AuthService ..> ForgotPasswordDto : Dependency
AuthService ..> OtpTypeCode : Dependency
AuthService ..> DestinationType : Dependency
AuthService ..> Bcrypt : Dependency

MailService --> MailerService : Association

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- users : Composition
PrismaService *-- otp_types : Composition
PrismaService *-- user_otps : Composition

users "0..1" o-- "0..*" user_otps : Aggregation
otp_types "1" o-- "0..*" user_otps : Aggregation
```

## 3.1.2.7 Class Diagram - Reset Password (`auth_reset_password`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class AuthController {
  -authService: AuthService
  +resetPassword(dto: ResetPasswordDto): Promise~any~
  ...
}

class ResetPasswordDto {
  +email: string
  +otp_code: string
  +new_password: string
}

class CreateNotificationDto {
  +user_ids: number[]
  +title: string
  +message: string
  +notification_type: string
  +reference_type: string?
  +reference_id: number?
}

class OtpTypeCode {
  <<enumeration>>
  RESET_PASSWORD
}

class NotificationType {
  <<enumeration>>
  SUCCESS
}

class AuthService {
  -prisma: PrismaService
  -notificationsService: NotificationsService
  +resetPassword(dto: ResetPasswordDto): Promise~any~
  ...
}

class Bcrypt {
  <<utility>>
  +hash(data: string, saltOrRounds: any): Promise~string~
  +compare(data: string, encrypted: string): Promise~boolean~
  +genSalt(rounds: number): Promise~string~
}

class NotificationsService {
  -prisma: PrismaService
  +createNotification(dto: CreateNotificationDto): Promise~any~
  ...
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
  +$transaction(callback: any): Promise~any~
  ...
}

class PrismaService {
  +users: PrismaUserDelegate
  +otp_types: PrismaOtpTypeDelegate
  +user_otps: PrismaUserOtpDelegate
  +notifications: PrismaNotificationDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class users {
  +user_id: Int
  +email: String
  +password_hash: String
  ...
}

class otp_types {
  +otp_type_id: Int
  +otp_type_code: String
  ...
}

class user_otps {
  +otp_id: BigInt
  +user_id: Int?
  +otp_type_id: Int
  +destination: String
  +otp_hash: String
  +is_verified: Boolean
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
  +is_read: Boolean
  ...
}

AuthController --> AuthService : Association
AuthController ..> ResetPasswordDto : Dependency

AuthService --> PrismaService : Association
AuthService --> NotificationsService : Association
AuthService ..> ResetPasswordDto : Dependency
AuthService ..> OtpTypeCode : Dependency
AuthService ..> NotificationType : Dependency
AuthService ..> CreateNotificationDto : Dependency
AuthService ..> Bcrypt : Dependency

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
otp_types "1" o-- "0..*" user_otps : Aggregation
users "1" o-- "0..*" notifications : Aggregation
```
