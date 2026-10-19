# Module 3.9: Education Content Feature (PlantUML)
> Contains 3 class diagrams.

## 3.9.1 Overview Class Diagram - Education Content Feature (`education_overview`)

```plantuml
@startuml
title 3.9.1 Overview Class Diagram - Education Content Feature
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class EducationController {
  -educationService: EducationService
  +getCategories(): Promise<any>
  +getDocuments(query: EducationFilterDto): Promise<any>
  +getDocumentBySlug(slug: string): Promise<any>
  +getRelatedDocuments(slug: string): Promise<any>
  +createCategory(dto: CreateEducationCategoryDto): Promise<any>
  +updateCategory(id: number, dto: UpdateEducationCategoryDto): Promise<any>
  +deleteCategory(id: number): Promise<any>
  +createDocument(req: any, dto: CreateEducationDocumentDto): Promise<any>
  +updateDocument(id: number, dto: UpdateEducationDocumentDto): Promise<any>
  +deleteDocument(id: number): Promise<any>
}

class EducationFilterDto {
  +page: number?
  +limit: number?
  +search: string?
  +category_id: number?
  +blood_type_id: number?
}

class CreateEducationCategoryDto {
  +category_name: string
  +description: string?
  +sort_order: number?
}

class UpdateEducationCategoryDto {
  +category_name: string?
  +description: string?
  +sort_order: number?
}

class CreateEducationDocumentDto {
  +title: string
  +slug: string
  +content_html: string
  +summary: string?
  +thumbnail_url: string?
  +category_id: number
  +blood_type_id: number?
  +is_published: boolean?
}

class UpdateEducationDocumentDto {
  +title: string?
  +slug: string?
  +content_html: string?
  +summary: string?
  +thumbnail_url: string?
  +category_id: number?
  +blood_type_id: number?
  +is_published: boolean?
}

class EducationService {
  -prisma: PrismaService
  +getCategories(): Promise<any>
  +createCategory(dto: CreateEducationCategoryDto): Promise<any>
  +updateCategory(id: number, dto: UpdateEducationCategoryDto): Promise<any>
  +deleteCategory(id: number): Promise<any>
  +getDocuments(query: EducationFilterDto): Promise<any>
  +getDocumentById(id: number): Promise<any>
  +getDocumentBySlug(slug: string): Promise<any>
  +getRelatedDocuments(slug: string): Promise<any>
  +createDocument(userId: number, dto: CreateEducationDocumentDto): Promise<any>
  +updateDocument(id: number, dto: UpdateEducationDocumentDto): Promise<any>
  +deleteDocument(id: number): Promise<any>
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
  +education_document_categories: PrismaEducationCategoryDelegate
  +education_documents: PrismaEducationDocumentDelegate
  +blood_types: PrismaBloodTypeDelegate
  +users: PrismaUserDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class education_document_categories {
  +category_id: Int
  +category_name: String
  +description: String?
  +sort_order: Int
  +education_documents: education_documents[]
}

class education_documents {
  +document_id: Int
  +category_id: Int
  +blood_type_id: Int?
  +title: String
  +slug: String
  +summary: String?
  +content_html: String
  +thumbnail_url: String?
  +view_count: Int
  +is_published: Boolean
  +published_at: DateTime?
  +created_by: Int?
  +created_at: DateTime
  +updated_at: DateTime?
  ...
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
  +abo: String
  +rh_factor: String
  +display_order: Int
  +is_active: Boolean
  ...
}

class users {
  +user_id: Int
  +full_name: String
  +avatar_url: String?
  +email: String
  +is_active: Boolean
  ...
}

EducationController --> EducationService : Association
EducationController ..> EducationFilterDto : Dependency
EducationController ..> CreateEducationCategoryDto : Dependency
EducationController ..> UpdateEducationCategoryDto : Dependency
EducationController ..> CreateEducationDocumentDto : Dependency
EducationController ..> UpdateEducationDocumentDto : Dependency
EducationService --> PrismaService : Association
EducationService ..> EducationFilterDto : Dependency
EducationService ..> CreateEducationCategoryDto : Dependency
EducationService ..> UpdateEducationCategoryDto : Dependency
EducationService ..> CreateEducationDocumentDto : Dependency
EducationService ..> UpdateEducationDocumentDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- education_document_categories : Composition
PrismaService *-- education_documents : Composition
PrismaService *-- blood_types : Composition
PrismaService *-- users : Composition
education_document_categories "1" o-- "0..*" education_documents : Aggregation
blood_types "0..1" o-- "0..*" education_documents : Aggregation
users "0..1" o-- "0..*" education_documents : Aggregation
@enduml
```

## 3.9.2.1 Class Diagram - Manage Education Categories (`education_categories`)

```plantuml
@startuml
title 3.9.2.1 Class Diagram - Manage Education Categories
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class EducationController {
  -educationService: EducationService
  ...
  +getCategories(): Promise<any>
  +createCategory(dto: CreateEducationCategoryDto): Promise<any>
  +updateCategory(id: number, dto: UpdateEducationCategoryDto): Promise<any>
  +deleteCategory(id: number): Promise<any>
  ...
}

class CreateEducationCategoryDto {
  +category_name: string
  +description: string?
  +sort_order: number?
}

class UpdateEducationCategoryDto {
  +category_name: string?
  +description: string?
  +sort_order: number?
}

class EducationService {
  -prisma: PrismaService
  ...
  +getCategories(): Promise<any>
  +createCategory(dto: CreateEducationCategoryDto): Promise<any>
  +updateCategory(id: number, dto: UpdateEducationCategoryDto): Promise<any>
  +deleteCategory(id: number): Promise<any>
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
  +education_document_categories: PrismaEducationCategoryDelegate
  +education_documents: PrismaEducationDocumentDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class education_document_categories {
  +category_id: Int
  +category_name: String
  +description: String?
  +sort_order: Int
  +education_documents: education_documents[]
}

class education_documents {
  +document_id: Int
  +category_id: Int
  +title: String
  +slug: String
  ...
}

EducationController --> EducationService : Association
EducationController ..> CreateEducationCategoryDto : Dependency
EducationController ..> UpdateEducationCategoryDto : Dependency
EducationService --> PrismaService : Association
EducationService ..> CreateEducationCategoryDto : Dependency
EducationService ..> UpdateEducationCategoryDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- education_document_categories : Composition
PrismaService *-- education_documents : Composition
education_document_categories "1" o-- "0..*" education_documents : Aggregation
@enduml
```

## 3.9.2.2 Class Diagram - View and Manage Education Documents (`education_documents`)

```plantuml
@startuml
title 3.9.2.2 Class Diagram - View and Manage Education Documents
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class EducationController {
  -educationService: EducationService
  ...
  +getDocuments(query: EducationFilterDto): Promise<any>
  +getDocumentBySlug(slug: string): Promise<any>
  +getRelatedDocuments(slug: string): Promise<any>
  +createDocument(req: any, dto: CreateEducationDocumentDto): Promise<any>
  +updateDocument(id: number, dto: UpdateEducationDocumentDto): Promise<any>
  +deleteDocument(id: number): Promise<any>
  ...
}

class EducationFilterDto {
  +page: number?
  +limit: number?
  +search: string?
  +category_id: number?
  +blood_type_id: number?
}

class CreateEducationDocumentDto {
  +title: string
  +slug: string
  +content_html: string
  +summary: string?
  +thumbnail_url: string?
  +category_id: number
  +blood_type_id: number?
  +is_published: boolean?
}

class UpdateEducationDocumentDto {
  +title: string?
  +slug: string?
  +content_html: string?
  +summary: string?
  +thumbnail_url: string?
  +category_id: number?
  +blood_type_id: number?
  +is_published: boolean?
}

class EducationService {
  -prisma: PrismaService
  ...
  +getDocuments(query: EducationFilterDto): Promise<any>
  +getDocumentById(id: number): Promise<any>
  +getDocumentBySlug(slug: string): Promise<any>
  +getRelatedDocuments(slug: string): Promise<any>
  +createDocument(userId: number, dto: CreateEducationDocumentDto): Promise<any>
  +updateDocument(id: number, dto: UpdateEducationDocumentDto): Promise<any>
  +deleteDocument(id: number): Promise<any>
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
  +education_documents: PrismaEducationDocumentDelegate
  +education_document_categories: PrismaEducationCategoryDelegate
  +blood_types: PrismaBloodTypeDelegate
  +users: PrismaUserDelegate
  ...
  +onModuleInit(): Promise<void>
  +onModuleDestroy(): Promise<void>
}

class education_documents {
  +document_id: Int
  +category_id: Int
  +blood_type_id: Int?
  +title: String
  +slug: String
  +summary: String?
  +content_html: String
  +thumbnail_url: String?
  +view_count: Int
  +is_published: Boolean
  +published_at: DateTime?
  +created_by: Int?
  +created_at: DateTime
  +updated_at: DateTime?
  ...
}

class education_document_categories {
  +category_id: Int
  +category_name: String
  +sort_order: Int
  ...
}

class blood_types {
  +blood_type_id: Int
  +blood_type_code: String
  +abo: String
  +rh_factor: String
  ...
}

class users {
  +user_id: Int
  +full_name: String
  +avatar_url: String?
  ...
}

EducationController --> EducationService : Association
EducationController ..> EducationFilterDto : Dependency
EducationController ..> CreateEducationDocumentDto : Dependency
EducationController ..> UpdateEducationDocumentDto : Dependency
EducationService --> PrismaService : Association
EducationService ..> EducationFilterDto : Dependency
EducationService ..> CreateEducationDocumentDto : Dependency
EducationService ..> UpdateEducationDocumentDto : Dependency
PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements
PrismaService *-- education_documents : Composition
PrismaService *-- education_document_categories : Composition
PrismaService *-- blood_types : Composition
PrismaService *-- users : Composition
education_document_categories "1" o-- "0..*" education_documents : Aggregation
blood_types "0..1" o-- "0..*" education_documents : Aggregation
users "0..1" o-- "0..*" education_documents : Aggregation
@enduml
```
