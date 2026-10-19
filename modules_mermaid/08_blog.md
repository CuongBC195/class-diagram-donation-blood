# Module 3.8: Blog Content Feature (Mermaid)
> Contains 5 class diagrams.

## 3.8.1 Overview Class Diagram - Blog Content Feature (`blog_overview`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class BlogController {
  -blogService: BlogService
  +getCategories(): Promise~any~
  +getAllPosts(query: BlogFilterDto): Promise~any~
  +getPostBySlug(slug: string): Promise~any~
  +getRelatedPosts(slug: string): Promise~any~
  +getComments(id: string, query: any): Promise~any~
  +addComment(id: number, req: any, body: AddCommentDto): Promise~any~
  +editMyComment(id: number, req: any, content: string): Promise~any~
  +deleteMyComment(id: number, req: any): Promise~any~
  +createCategory(dto: CreateCategoryDto): Promise~any~
  +updateCategory(id: number, dto: UpdateCategoryDto): Promise~any~
  +deleteCategory(id: number): Promise~any~
  +createPost(req: any, dto: CreatePostDto): Promise~any~
  +updatePost(postId: number, dto: UpdatePostDto): Promise~any~
  +deletePost(postId: number): Promise~any~
  +getAdminComments(query: any): Promise~any~
  +approveComment(id: number, isApproved: boolean): Promise~any~
  +deleteAdminComment(id: number): Promise~any~
}

class BlogService {
  -prisma: PrismaService
  +getCategories(): Promise~any~
  +createCategory(dto: CreateCategoryDto): Promise~any~
  +updateCategory(id: number, dto: UpdateCategoryDto): Promise~any~
  +deleteCategory(id: number): Promise~any~
  +getAllPosts(query: BlogFilterDto): Promise~any~
  +getPostBySlug(slug: string): Promise~any~
  +getRelatedPosts(slug: string): Promise~any~
  +createPost(userId: number, dto: CreatePostDto): Promise~any~
  +updatePost(postId: number, dto: UpdatePostDto): Promise~any~
  +deletePost(postId: number): Promise~any~
  +getComments(postId: number, query: any): Promise~any~
  +addComment(postId: number, userId: number | null, data: AddCommentDto): Promise~any~
  +editComment(commentId: number, userId: number, content: string): Promise~any~
  +deleteMyComment(commentId: number, userId: number): Promise~any~
  +getAdminComments(query: any): Promise~any~
  +approveComment(commentId: number, isApproved: boolean): Promise~any~
  +deleteAdminComment(commentId: number): Promise~any~
}

class BlogFilterDto {
  +category_id: number?
  +search: string?
  +page: number?
  +limit: number?
}

class CreateCategoryDto {
  +category_name: string
  +slug: string
}

class UpdateCategoryDto {
  +category_name: string?
  +slug: string?
}

class CreatePostDto {
  +blog_category_id: number
  +title: string
  +slug: string
  +content: string
  +summary: string?
  +thumbnail_url: string?
  +is_published: boolean?
}

class UpdatePostDto {
  +blog_category_id: number?
  +title: string?
  +slug: string?
  +content: string?
  +summary: string?
  +thumbnail_url: string?
  +is_published: boolean?
}

class AddCommentDto {
  +content: string
  +guest_name: string?
  +parent_comment_id: number?
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
  +blog_categories: PrismaBlogCategoryDelegate
  +blog_posts: PrismaBlogPostDelegate
  +blog_comments: PrismaBlogCommentDelegate
  +users: PrismaUserDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class blog_categories {
  +blog_category_id: Int
  +category_name: String
  +slug: String
}

class blog_posts {
  +post_id: Int
  +blog_category_id: Int
  +author_user_id: Int?
  +title: String
  +slug: String
  +summary: String?
  +content_html: String
  +thumbnail_url: String?
  +view_count: Int
  +is_published: Boolean
  +published_at: DateTime?
  +category: blog_categories
  +author: users?
  ...
}

class blog_comments {
  +comment_id: Int
  +post_id: Int
  +parent_comment_id: Int?
  +user_id: Int?
  +reply_to_user_id: Int?
  +guest_name: String?
  +content: String
  +is_approved: Boolean
  +created_at: DateTime
  +post: blog_posts
  +user: users?
  ...
}

class users {
  +user_id: Int
  +full_name: String
  ...
}

BlogController --> BlogService : Association
BlogController ..> BlogFilterDto : Dependency
BlogController ..> CreateCategoryDto : Dependency
BlogController ..> UpdateCategoryDto : Dependency
BlogController ..> CreatePostDto : Dependency
BlogController ..> UpdatePostDto : Dependency
BlogController ..> AddCommentDto : Dependency

BlogService --> PrismaService : Association
BlogService ..> BlogFilterDto : Dependency
BlogService ..> CreateCategoryDto : Dependency
BlogService ..> UpdateCategoryDto : Dependency
BlogService ..> CreatePostDto : Dependency
BlogService ..> UpdatePostDto : Dependency
BlogService ..> AddCommentDto : Dependency

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- blog_categories : Composition
PrismaService *-- blog_posts : Composition
PrismaService *-- blog_comments : Composition
PrismaService *-- users : Composition

blog_categories "1" o-- "0..*" blog_posts : Aggregation
users "1" o-- "0..*" blog_posts : Aggregation
blog_posts "1" o-- "0..*" blog_comments : Aggregation
users "0..1" o-- "0..*" blog_comments : Aggregation
blog_comments "0..1" o-- "0..*" blog_comments : Aggregation
```

## 3.8.2.1 Class Diagram - Manage Blog Categories (`blog_categories`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class BlogController {
  -blogService: BlogService
  +getCategories(): Promise~any~
  +createCategory(dto: CreateCategoryDto): Promise~any~
  +updateCategory(id: number, dto: UpdateCategoryDto): Promise~any~
  +deleteCategory(id: number): Promise~any~
  ...
}

class CreateCategoryDto {
  +category_name: string
  +slug: string
}

class UpdateCategoryDto {
  +category_name: string?
  +slug: string?
}

class BlogService {
  -prisma: PrismaService
  +getCategories(): Promise~any~
  +createCategory(dto: CreateCategoryDto): Promise~any~
  +updateCategory(id: number, dto: UpdateCategoryDto): Promise~any~
  +deleteCategory(id: number): Promise~any~
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
  +blog_categories: PrismaBlogCategoryDelegate
  +blog_posts: PrismaBlogPostDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class blog_posts {
  +post_id: Int
  +category_id: Int
  +title: String
  +slug: String
  ...
}

class blog_categories {
  +blog_category_id: Int
  +category_name: String
  +slug: String
  ...
}

BlogController --> BlogService : Association
BlogController ..> CreateCategoryDto : Dependency
BlogController ..> UpdateCategoryDto : Dependency

BlogService --> PrismaService : Association
BlogService ..> CreateCategoryDto : Dependency
BlogService ..> UpdateCategoryDto : Dependency

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- blog_categories : Composition
PrismaService *-- blog_posts : Composition

blog_categories "1" o-- "0..*" blog_posts : Aggregation
```

## 3.8.2.2 Class Diagram - View and Manage Blog Posts (`blog_posts`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class BlogController {
  -blogService: BlogService
  +getAllPosts(query: BlogFilterDto): Promise~any~
  +getPostBySlug(slug: string): Promise~any~
  +getRelatedPosts(slug: string): Promise~any~
  +createPost(req: any, dto: CreatePostDto): Promise~any~
  +updatePost(postId: number, dto: UpdatePostDto): Promise~any~
  +deletePost(postId: number): Promise~any~
  ...
}

class BlogFilterDto {
  +category_id: number?
  +search: string?
  +page: number?
  +limit: number?
}

class CreatePostDto {
  +blog_category_id: number
  +title: string
  +slug: string
  +content: string
  +summary: string?
  +thumbnail_url: string?
  +is_published: boolean?
}

class UpdatePostDto {
  +blog_category_id: number?
  +title: string?
  +slug: string?
  +content: string?
  +summary: string?
  +thumbnail_url: string?
  +is_published: boolean?
}

class BlogService {
  -prisma: PrismaService
  +getAllPosts(query: BlogFilterDto): Promise~any~
  +getPostBySlug(slug: string): Promise~any~
  +getRelatedPosts(slug: string): Promise~any~
  +createPost(userId: number, dto: CreatePostDto): Promise~any~
  +updatePost(postId: number, dto: UpdatePostDto): Promise~any~
  +deletePost(postId: number): Promise~any~
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
  +blog_categories: PrismaBlogCategoryDelegate
  +blog_posts: PrismaBlogPostDelegate
  +users: PrismaUserDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class blog_categories {
  +blog_category_id: Int
  +category_name: String
  +slug: String
  ...
}

class blog_posts {
  +post_id: Int
  +blog_category_id: Int
  +author_user_id: Int?
  +title: String
  +slug: String
  +summary: String?
  +content_html: String
  +thumbnail_url: String?
  +is_published: Boolean
  +published_at: DateTime?
  +category: blog_categories
  +author: users?
  ...
}

class users {
  +user_id: Int
  +full_name: String
  ...
}

BlogController --> BlogService : Association
BlogController ..> BlogFilterDto : Dependency
BlogController ..> CreatePostDto : Dependency
BlogController ..> UpdatePostDto : Dependency

BlogService --> PrismaService : Association
BlogService ..> BlogFilterDto : Dependency
BlogService ..> CreatePostDto : Dependency
BlogService ..> UpdatePostDto : Dependency

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- blog_categories : Composition
PrismaService *-- blog_posts : Composition
PrismaService *-- users : Composition

blog_categories "1" o-- "0..*" blog_posts : Aggregation
users "1" o-- "0..*" blog_posts : Aggregation
```

## 3.8.2.3 Class Diagram - User Comment Interactions (`blog_comments_user`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class BlogController {
  -blogService: BlogService
  +getComments(id: string, query: any): Promise~any~
  +addComment(id: number, req: any, body: AddCommentDto): Promise~any~
  +editMyComment(id: number, req: any, content: string): Promise~any~
  +deleteMyComment(id: number, req: any): Promise~any~
  ...
}

class AddCommentDto {
  +content: string
  +guest_name: string?
  +parent_comment_id: number?
}

class BlogService {
  -prisma: PrismaService
  +getComments(postId: number, query: any): Promise~any~
  +addComment(postId: number, userId: number | null, data: AddCommentDto): Promise~any~
  +editComment(commentId: number, userId: number, content: string): Promise~any~
  +deleteMyComment(commentId: number, userId: number): Promise~any~
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
  +blog_comments: PrismaBlogCommentDelegate
  +blog_posts: PrismaBlogPostDelegate
  +users: PrismaUserDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class blog_comments {
  +comment_id: Int
  +post_id: Int
  +parent_comment_id: Int?
  +user_id: Int?
  +guest_name: String?
  +content: String
  +is_approved: Boolean
  +created_at: DateTime
  +post: blog_posts
  +user: users?
  ...
}

class blog_posts {
  +post_id: Int
  +title: String
  ...
}

class users {
  +user_id: Int
  +full_name: String
  ...
}

BlogController --> BlogService : Association
BlogController ..> AddCommentDto : Dependency

BlogService --> PrismaService : Association
BlogService ..> AddCommentDto : Dependency

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- blog_comments : Composition
PrismaService *-- blog_posts : Composition
PrismaService *-- users : Composition

blog_posts "1" o-- "0..*" blog_comments : Aggregation
users "0..1" o-- "0..*" blog_comments : Aggregation
blog_comments "0..1" o-- "0..*" blog_comments : Aggregation
```

## 3.8.2.4 Class Diagram - Admin Comment Moderation (`blog_comments_admin`)

```mermaid
%%{init: {"theme":"base","themeVariables":{"background":"#ffffff","primaryColor":"#ffffff","primaryTextColor":"#111111","primaryBorderColor":"#111111","lineColor":"#111111","secondaryColor":"#ffffff","tertiaryColor":"#ffffff","edgeLabelBackground":"#ffffff","labelBoxBkgColor":"#ffffff","fontFamily":"Arial"}}}%%
classDiagram
direction TB

class BlogController {
  -blogService: BlogService
  +getAdminComments(query: any): Promise~any~
  +approveComment(id: number, isApproved: boolean): Promise~any~
  +deleteAdminComment(id: number): Promise~any~
  ...
}

class BlogService {
  -prisma: PrismaService
  +getAdminComments(query: any): Promise~any~
  +approveComment(commentId: number, isApproved: boolean): Promise~any~
  +deleteAdminComment(commentId: number): Promise~any~
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
  +blog_comments: PrismaBlogCommentDelegate
  +blog_posts: PrismaBlogPostDelegate
  +users: PrismaUserDelegate
  +onModuleInit(): Promise~void~
  +onModuleDestroy(): Promise~void~
}

class blog_comments {
  +comment_id: Int
  +post_id: Int
  +user_id: Int?
  +parent_comment_id: Int?
  +content: String
  +is_approved: Boolean
  +created_at: DateTime
  +post: blog_posts
  +user: users?
  ...
}

class blog_posts {
  +post_id: Int
  +title: String
  ...
}

class users {
  +user_id: Int
  +full_name: String
  +email: String
  ...
}

BlogController --> BlogService : Association

BlogService --> PrismaService : Association

PrismaService --|> PrismaClient : Inheritance
PrismaService ..|> OnModuleInit : Implements
PrismaService ..|> OnModuleDestroy : Implements

PrismaService *-- blog_comments : Composition
PrismaService *-- blog_posts : Composition
PrismaService *-- users : Composition

blog_posts "1" o-- "0..*" blog_comments : Aggregation
users "0..1" o-- "0..*" blog_comments : Aggregation
```
