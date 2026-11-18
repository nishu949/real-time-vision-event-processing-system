# Real-Time Vision Event Processing System

A real-time computer vision application built using Python and OpenCV that detects motion from a live camera feed, generates motion events, captures evidence snapshots, logs event metadata into a database, and monitors processing performance.

---

## Overview

This project demonstrates the design of a vision-based event processing pipeline commonly found in security monitoring, surveillance, and industrial inspection systems.

The application continuously captures frames from a webcam, performs image processing operations to detect motion, generates events when movement is detected, stores event information in an SQLite database, and publishes event notifications through a lightweight event bus.

---

## Key Features

✅ Real-Time Video Stream Processing

✅ Motion Detection using Frame Differencing

✅ Image Processing with OpenCV

✅ Bounding Box Visualization

✅ Automatic Snapshot Capture

✅ SQLite Event Logging

✅ Event Publishing Mechanism

✅ FPS (Frames Per Second) Monitoring

✅ Motion Event Throttling (Cooldown System)

✅ Modular and Maintainable Architecture

---

## System Architecture

```text
Camera Feed
     │
     ▼
Frame Capture
     │
     ▼
Image Processing
(GrayScale + Blur + Threshold)
     │
     ▼
Motion Detection
     │
     ▼
Contour Analysis
     │
     ▼
Event Generation
     │
 ┌───┼───────────────┐
 │   │               │
 ▼   ▼               ▼
Save Image      Database Log     Event Publisher
 │                   │               │
 ▼                   ▼               ▼
Snapshots       SQLite DB      Console / Log Events
```

---

## Project Structure

```text
vision-event-system/

├── app.py
├── detector.py
├── database.py
├── event_bus.py
├── requirements.txt
│
├── database/
│   └── events.db
│
├── snapshots/
│   └── motion_images
│
└── logs/
    └── pipeline.log
```

---

## Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| OpenCV | Computer Vision & Image Processing |
| SQLite | Event Storage |
| NumPy | Numerical Operations |
| Logging | Event Monitoring |

---

## Motion Detection Workflow

### Step 1: Capture Frames

The webcam continuously captures consecutive frames.

```text
Frame A
Frame B
```

---

### Step 2: Calculate Difference

The application compares the two frames.

```python
cv2.absdiff(frame1, frame2)
```

Only changed regions remain visible.

---

### Step 3: Convert to Grayscale

Color information is removed to reduce processing complexity.

```python
cv2.cvtColor(...)
```

---

### Step 4: Noise Reduction

Gaussian Blur is applied to smooth the image.

```python
cv2.GaussianBlur(...)
```

---

### Step 5: Thresholding

The processed image is converted into a binary representation.

```python
cv2.threshold(...)
```

Pixels become either black or white.

---

### Step 6: Contour Extraction

The system identifies boundaries of moving objects.

```python
cv2.findContours(...)
```

---

### Step 7: Event Generation

When significant motion is detected:

- Bounding box is drawn
- Event is generated
- Snapshot is stored
- Event is logged
- Notification is published

---

## Database Schema

The application stores motion events using SQLite.

### events

| Column | Type |
|----------|----------|
| id | INTEGER |
| event_type | TEXT |
| timestamp | TEXT |
| image_path | TEXT |

Example:

```text
1 | MOTION | 2026-11-18 18:45:20 | snapshots/img1.jpg
```

---

## Event Publishing

A lightweight event bus has been implemented to simulate event-driven systems.

Sample Event:

```text
[EVENT]
Motion detected -> snapshots/20261118_184520.jpg
```

This architecture can later be extended using:

- Apache Kafka
- RabbitMQ
- WebSockets
- MQTT

---

## Performance Monitoring

The application continuously measures FPS.

```text
FPS = Frames Processed Per Second
```

This metric is used to evaluate real-time processing performance.

Example:

```text
FPS: 30
```

Meaning:

```text
30 frames processed every second
```

---

## Cooldown Mechanism

To avoid generating duplicate events while motion persists, the application enforces a cooldown period between consecutive events.

Benefits:

- Prevents unnecessary database writes
- Prevents duplicate images
- Reduces alert flooding
- Improves system efficiency

---

## Installation

### Clone Repository

```bash
git clone https://github.com/nishu949/real-time-vision-event-processing-system.git
```

### Navigate to Project

```bash
cd real-time-vision-event-processing-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## Sample Dashboard

```text
Events: 7
Status: Motion Detected
18:45:20
FPS: 31
```

---

## Future Improvements

- YOLO Object Detection
- Face Recognition
- WebSocket Notifications
- Kafka Event Streaming
- Cloud Database Integration
- Multi-Camera Support
- Streamlit Dashboard
- Docker Deployment

---

## Learning Outcomes

Through this project, the following concepts were explored:

- Computer Vision Fundamentals
- OpenCV Framework
- Real-Time Video Processing
- Image Processing Techniques
- Contour Detection
- Event-Driven Architecture
- Database Integration
- Performance Monitoring
- Modular Python Development

---

## Author

**Nishant**

Real-Time Vision Event Processing System

Built using Python, OpenCV, and SQLite.
