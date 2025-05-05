# FastAPI API Versioning Template

A comprehensive demonstration of API versioning strategies in FastAPI, showcasing three different approaches to help developers choose the right architecture for their needs.

## 🎯 Purpose

This template demonstrates the evolution of API versioning from basic to advanced implementations, helping developers:
- Understand different versioning strategies
- Maintain backward compatibility
- Scale APIs effectively
- Choose the right approach based on project size

##  Project Structure

```
fastapi-template/
├── proj_1/              # Basic API versioning
│   └── main.py         # All-in-one implementation
├── proj_2/              # Structured versioning
│   └── app/
│       ├── controllers/  # Route handlers
│       ├── services/    # Business logic
│       └── models/      # Data schemas
├── proj_3/              # Full modular versioning
│   └── app/
│       ├── controllers/
│       │   ├── v1/     # Version 1 routes
│       │   └── v2/     # Version 2 routes
│       ├── services/
│       │   ├── v1/     # Version 1 business logic
│       │   └── v2/     # Version 2 business logic
│       └── models/     # Shared data models
└── main.py             # Example of problematic versioning
```

## ⚡ Quick Start

1. **Clone and Setup**
```bash
git clone https://github.com/rahulsamant37/FASTAPI_versioning-Template.git
cd FASTAPI_versioning-Template
uv venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
```

2. **Install Dependencies**
```bash
uv add fastapi
```

3. **Run Any Example**
```bash
# Basic versioning (Project 1)
uvicorn proj_1.main:app --reload

# Structured versioning (Project 2)
uvicorn proj_2.app.main:app --reload

# Full modular versioning (Project 3)
uvicorn proj_3.app.main:app --reload
```

## 🔗 API Endpoints

### V1 API (`/api/v1`)
| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/users` | List all users | `List[UserV1]` |
| GET | `/users/{id}` | Get user by ID | `UserV1` |

### V2 API (`/api/v2`)
| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/users` | List all users with email | `List[UserV2]` |
| GET | `/users/{id}` | Get user by ID with email | `UserV2]` |

## 🛠️ Implementation Approaches

### 1. Basic Router-based (proj_1)
- Single file implementation
- Uses FastAPI's `APIRouter`
- Suitable for: Small APIs, Prototypes
- Pros: Simple, Quick to implement
- Cons: Limited scalability

### 2. Structured (proj_2)
- MVC-like architecture
- Shared service layer
- Suitable for: Medium-sized APIs
- Pros: Good organization, Maintainable
- Cons: Some version coupling

### 3. Full Modular (proj_3)
- Complete version isolation
- Independent services per version
- Suitable for: Large APIs, Enterprise
- Pros: Highly maintainable, Scalable
- Cons: More complex setup

## 📋 Technical Details

### Dependencies
```toml
python = ">=3.12"
fastapi = ">=0.115.12"
pydantic = ">=2.0.0"
uvicorn = ">=0.24.0"
email-validator = ">=2.0.0"  # For email validation
```

### Key Features
- ✅ Type-safe with Pydantic models
- ✅ Async/await support
- ✅ OpenAPI documentation
- ✅ Dependency injection
- ✅ Clear version boundaries

## 📚 Documentation

- **API Documentation**: Available at `/docs` (Swagger) and `/redoc` (ReDoc)
- **Version Management**: 
  - V1: Basic user info (id, name)
  - V2: Extended user info (id, name, email)

## 🔍 Best Practices

1. **Version Prefixing**
   - Clear URL versioning (`/api/v1`, `/api/v2`)
   - Consistent version naming

2. **Code Organization**
   - Separation of concerns
   - Clear module boundaries
   - Version-specific services

3. **Type Safety**
   - Pydantic models for validation
   - Comprehensive type hints
   - Version-specific schemas

4. **Backward Compatibility**
   - Maintained across versions
   - Clear upgrade paths
   - Version-specific responses

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.