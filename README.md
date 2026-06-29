# CloudBench - Multi-Cloud Cost Estimator ☁️

A web-based application that estimates and compares cloud infrastructure costs across major cloud providers including AWS, Microsoft Azure, and Google Cloud Platform (GCP).

## 🚀 Features

* Compare estimated monthly costs across **AWS**, **Azure**, and **GCP**.
* Supports user inputs for:

  * CPU Cores
  * RAM (GB)
  * Storage (GB)
  * Usage Hours per Month
  * Deployment Region
* Region-based pricing adjustments.
* Automatic recommendation of the **most cost-effective provider**.
* Clean and responsive user interface.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Templating Engine:** Jinja2
* **Version Control:** Git, GitHub

## 📂 Project Structure

```text
CloudBench-Multi-Cloud-Cost-Estimator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ Installation and Setup

### Clone the repository

```bash
git clone https://github.com/Abhinayasree05/CloudBench-Multi-Cloud-Cost-Estimator.git
```

### Navigate to the project directory

```bash
cd CloudBench-Multi-Cloud-Cost-Estimator
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

### Open in browser

```text
http://127.0.0.1:5000
```

## 📊 How It Works

1. Enter infrastructure requirements such as CPU, RAM, Storage, and Usage Hours.
2. Select the desired deployment region.
3. The application estimates monthly costs for AWS, Azure, and GCP using predefined pricing models.
4. The system recommends the provider with the lowest estimated cost.

## 🎯 Example Inputs

* CPU Cores: 4
* RAM: 16 GB
* Storage: 100 GB
* Usage Hours: 720 Hours
* Region: US-East

## 📈 Future Enhancements

* Integration with real-time cloud pricing APIs.
* Currency conversion support.
* Cost visualization using graphs and charts.
* PDF report export functionality.
* Support for additional cloud providers.

## 👩‍💻 Author

**Abhinayasree**

GitHub: https://github.com/Abhinayasree05


