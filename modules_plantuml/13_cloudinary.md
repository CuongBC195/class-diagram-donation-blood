# Module 3.13: File Upload Feature (PlantUML)
> Contains 2 class diagrams.

## 3.13.1 Overview Class Diagram - File Upload Feature (`cloudinary_overview`)

```plantuml
@startuml
title 3.13.1 Overview Class Diagram - File Upload Feature
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class CloudinaryController {
  -cloudinaryService: CloudinaryService
  +uploadImage(file: Express.Multer.File): Promise<any>
}

class CloudinaryService {
  +uploadFile(file: Express.Multer.File): Promise<any>
}

class CloudinaryProvider <<utility>> {
  +provide: string
  +useFactory(): any
}

class CloudinarySDK <<utility>> {
  +config(options: object): any
  +upload_stream(callback: any): any
}

CloudinaryController --> CloudinaryService : Association
CloudinaryService ..> CloudinaryProvider : Dependency
CloudinaryService ..> CloudinarySDK : Dependency
CloudinaryProvider ..> CloudinarySDK : Dependency
@enduml
```

## 3.13.2.1 Class Diagram - Upload Image (`cloudinary_upload`)

```plantuml
@startuml
title 3.13.2.1 Class Diagram - Upload Image
skinparam classAttributeIconSize 0
skinparam monochrome true
skinparam shadowing false
skinparam defaultFontName Arial
hide empty members

class CloudinaryController {
  -cloudinaryService: CloudinaryService
  +uploadImage(file: Express.Multer.File): Promise<any>
}

class CloudinaryService {
  +uploadFile(file: Express.Multer.File): Promise<any>
}

class CloudinaryProvider <<utility>> {
  +provide: string
  +useFactory(): any
}

class CloudinarySDK <<utility>> {
  +config(options: object): any
  +upload_stream(callback: any): any
}

CloudinaryController --> CloudinaryService : Association
CloudinaryService ..> CloudinaryProvider : Dependency
CloudinaryService ..> CloudinarySDK : Dependency
CloudinaryProvider ..> CloudinarySDK : Dependency
@enduml
```
