# Dr.MeD - Backend API Documentation

## Overview
This document provides complete specifications for integrating the backend with the Dr.MeD frontend.

## Base URL
```
http://localhost:5000/api
```

## Authentication
All endpoints require authentication using Bearer token (optional for hackathon demo).

```
Authorization: Bearer YOUR_JWT_TOKEN
```

---

## Endpoints

### 1. Upload Medical Report

**Endpoint:** `POST /api/upload-report`

**Description:** Upload a medical report file (PDF, JPG, PNG) for processing.

**Request:**
```
Content-Type: multipart/form-data

Fields:
- report: File (PDF, JPG, PNG)
- patientData: JSON string
  {
    "name": "John Doe",
    "age": 45,
    "condition": "Diabetes",
    "literacyLevel": "Medium (Educated Patient)"
  }
```

**Response:**
```json
{
  "success": true,
  "fileId": "report_12345_1234567890",
  "fileName": "blood_test_report.pdf",
  "uploadedAt": "2026-02-20T10:30:00Z",
  "message": "File uploaded successfully"
}
```

---

### 2. Analyze Medical Report

**Endpoint:** `POST /api/analyze`

**Description:** Analyze uploaded medical report using AI models.

**Request:**
```json
{
  "fileId": "report_12345_1234567890",
  "patientContext": {
    "name": "John Doe",
    "age": 45,
    "condition": "Diabetes",
    "literacyLevel": "Medium (Educated Patient)"
  },
  "models": {
    "nlp": true,
    "classifier": true,
    "risk": true,
    "rag": true,
    "personalization": true,
    "confidence": true
  }
}
```

**Response:**
```json
{
  "success": true,
  "confidence": 96,
  "analysisId": "analysis_12345",
  "findings": [
    {
      "label": "Blood Glucose (Fasting)",
      "value": "105 mg/dL",
      "status": "normal",
      "normalRange": "70-100 mg/dL",
      "unit": "mg/dL"
    },
    {
      "label": "HbA1c",
      "value": "6.2%",
      "status": "normal",
      "normalRange": "<5.7%",
      "unit": "%"
    },
    {
      "label": "Total Cholesterol",
      "value": "215 mg/dL",
      "status": "warning",
      "normalRange": "<200 mg/dL",
      "unit": "mg/dL"
    }
  ],
  "analysis": "Based on your comprehensive blood work analysis, your overall health indicators show positive trends...",
  "recommendations": [
    {
      "title": "Dietary Adjustments",
      "description": "Consider increasing fiber intake and reducing saturated fats...",
      "icon": "🥗",
      "priority": "high"
    },
    {
      "title": "Physical Activity",
      "description": "Maintain current exercise routine of 30 minutes daily...",
      "icon": "🏃",
      "priority": "medium"
    }
  ],
  "uncertainties": [
    "Slight elevation in LDL cholesterol - recommend lipid panel retest in 3 months",
    "Vitamin D levels not included in current report - may need separate test"
  ],
  "riskScore": {
    "cardiovascular": 0.15,
    "diabetes": 0.32,
    "overall": 0.25
  },
  "processedAt": "2026-02-20T10:31:25Z"
}
```

---

### 3. Get Patient History

**Endpoint:** `GET /api/patient/history?patientId={id}`

**Description:** Retrieve patient's previous medical reports and analyses.

**Response:**
```json
{
  "success": true,
  "patientId": "patient_12345",
  "history": [
    {
      "date": "2026-02-20",
      "reportType": "Blood Test",
      "analysisId": "analysis_12345",
      "summary": "Glucose control improved by 18%"
    },
    {
      "date": "2025-11-15",
      "reportType": "Blood Test",
      "analysisId": "analysis_11234",
      "summary": "Initial diabetes diagnosis"
    }
  ]
}
```

---

### 4. Doctor Verification

**Endpoint:** `POST /api/doctor/verify`

**Description:** Submit analysis for doctor verification.

**Request:**
```json
{
  "analysisId": "analysis_12345",
  "doctorId": "doctor_789",
  "notes": "This AI analysis is accurate and comprehensive..."
}
```

**Response:**
```json
{
  "success": true,
  "verificationId": "verify_456",
  "verifiedAt": "2026-02-20T14:45:00Z",
  "doctorInfo": {
    "name": "Dr. Sarah Johnson, MD",
    "specialty": "Endocrinologist",
    "experience": "15 years",
    "licenseNo": "MD-456789"
  }
}
```

---

### 5. Get Recommendations

**Endpoint:** `GET /api/recommendations?analysisId={id}`

**Description:** Get personalized health recommendations based on analysis.

**Response:**
```json
{
  "success": true,
  "recommendations": [
    {
      "category": "diet",
      "title": "Dietary Adjustments",
      "description": "Increase fiber intake...",
      "icon": "🥗",
      "priority": "high"
    }
  ]
}
```

---

### 6. Save Analysis

**Endpoint:** `POST /api/analysis/save`

**Description:** Save analysis results to database.

**Request:**
```json
{
  "analysisId": "analysis_12345",
  "patientId": "patient_12345",
  "reportData": { ... }
}
```

**Response:**
```json
{
  "success": true,
  "savedAt": "2026-02-20T10:32:00Z",
  "recordId": "record_67890"
}
```

---

## AI Model Endpoints

### 1. NLP Text Extraction

**Endpoint:** `POST /api/models/nlp/extract`

**Description:** Extract structured information from medical report text using NLP.

**Request:**
```json
{
  "text": "Patient blood glucose level is 105 mg/dL...",
  "extractionType": "full"
}
```

**Response:**
```json
{
  "entities": [
    {
      "type": "measurement",
      "name": "Blood Glucose",
      "value": 105,
      "unit": "mg/dL"
    }
  ],
  "structure": { ... }
}
```

---

### 2. Classification Model

**Endpoint:** `POST /api/models/classify`

**Description:** Classify medical condition from report data.

**Request:**
```json
{
  "features": {
    "glucose": 105,
    "hba1c": 6.2,
    "age": 45
  }
}
```

**Response:**
```json
{
  "condition": "Type 2 Diabetes",
  "confidence": 0.92,
  "severity": "mild"
}
```

---

### 3. Risk Assessment

**Endpoint:** `POST /api/models/risk-assessment`

**Description:** Assess health risks based on medical data.

**Request:**
```json
{
  "patientData": { ... },
  "medicalHistory": [ ... ]
}
```

**Response:**
```json
{
  "riskScores": {
    "cardiovascular": 0.15,
    "diabetes": 0.32,
    "kidney": 0.08
  },
  "recommendations": [ ... ]
}
```

---

### 4. RAG Query

**Endpoint:** `POST /api/rag/query`

**Description:** Query Retrieval Augmented Generation system for medical context.

**Request:**
```json
{
  "query": "What does HbA1c level of 6.2% indicate?",
  "context": "diabetes management"
}
```

**Response:**
```json
{
  "answer": "An HbA1c level of 6.2% indicates...",
  "sources": [
    {
      "title": "ADA Diabetes Guidelines 2025",
      "url": "https://...",
      "relevance": 0.95
    }
  ]
}
```

---

### 5. Personalization

**Endpoint:** `POST /api/models/personalize`

**Description:** Personalize explanation based on patient literacy and context.

**Request:**
```json
{
  "content": "HbA1c: 6.2%",
  "patientProfile": {
    "age": 45,
    "literacyLevel": "medium",
    "condition": "diabetes"
  }
}
```

**Response:**
```json
{
  "personalizedContent": "Your HbA1c is 6.2%, which means your average blood sugar over the past 3 months is in a good range for someone managing diabetes..."
}
```

---

### 6. Confidence Scoring

**Endpoint:** `POST /api/models/confidence`

**Description:** Calculate confidence score and detect potential hallucinations.

**Request:**
```json
{
  "analysis": "Patient glucose levels indicate...",
  "sourceData": { ... }
}
```

**Response:**
```json
{
  "confidenceScore": 0.96,
  "hallucinationRisk": "low",
  "verifiedStatements": 45,
  "uncertainStatements": 2
}
```

---

## Error Responses

All endpoints return standard error format:

```json
{
  "success": false,
  "error": {
    "code": "INVALID_FILE_FORMAT",
    "message": "Only PDF, JPG, and PNG files are supported",
    "details": "..."
  }
}
```

### Common Error Codes
- `INVALID_FILE_FORMAT` - Unsupported file type
- `FILE_TOO_LARGE` - File exceeds 10MB limit
- `ANALYSIS_FAILED` - AI model processing failed
- `UNAUTHORIZED` - Invalid or missing authentication
- `RATE_LIMIT_EXCEEDED` - Too many requests

---

## Rate Limits
- Free tier: 10 requests/minute
- Pro tier: 100 requests/minute
- Enterprise: Unlimited

---

## WebSocket Support (Optional)

For real-time analysis updates:

```javascript
const ws = new WebSocket('ws://localhost:5000/ws/analysis');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Analysis progress:', data.progress);
};
```

---

## Testing

Use the mock data functions in the frontend when backend is not available. The frontend will automatically fall back to demo mode if API calls fail.

## Security Considerations

1. Always use HTTPS in production
2. Implement rate limiting
3. Sanitize file uploads
4. Validate patient data
5. Encrypt sensitive medical information
6. Implement HIPAA compliance measures
7. Use secure authentication (JWT, OAuth2)
