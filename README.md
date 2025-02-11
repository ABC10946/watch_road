# Motion Detection Application

This project implements a motion detection application using OpenCV and exports metrics to Prometheus for monitoring. The application captures video from a specified source, detects motion, and provides real-time metrics on detected motion events.

## Project Structure

```
motion-detection-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── motion_detector.py     # Contains the MotionDetector class for motion detection
│   ├── prometheus_metrics.py  # Defines the PrometheusMetrics class for metrics export
│   └── __init__.py           # Marks the directory as a Python package
├── requirements.txt          # Lists project dependencies
└── README.md                 # Documentation for the project
```

## Requirements

To run this project, you need to install the following dependencies:

- OpenCV
- Prometheus client
- Other necessary libraries

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

   ```
   git clone <repository-url>
   cd motion-detection-app
   ```

2. Install the required dependencies.

3. Run the application:

   ```
   python src/main.py
   ```

4. Access the Prometheus metrics at `http://localhost:8000/metrics`.

## Example

Once the application is running, it will start detecting motion in the video feed. When motion is detected, metrics will be updated and can be scraped by a Prometheus server.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.