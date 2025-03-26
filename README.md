# Multi_Modal_using_Ollama

Here’s a README for your GitHub project that includes the steps for creating a virtual environment (optional), downloading Ollama and models, starting the server, and executing the main script:

---

# Project Name

## Description

This project leverages **Ollama**, an advanced AI model interaction tool. It allows you to run and interact with various machine learning models, such as **Llama 3B** and **DeepSeek**. Follow the steps below to set up your environment and start using the project.

## Requirements

- Python 3.x
- Ollama (for running models)
- Command Prompt or Terminal access

## Setup Instructions

### 1. Create a Virtual Environment (Optional but Recommended)

It’s recommended to create a virtual environment to keep dependencies isolated. However, this step is optional.

#### Using `venv` (Python's built-in virtual environment tool)

1. Navigate to the project directory:
   ```bash
   cd path/to/your/project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### 2. Download Ollama

You need **Ollama** to run the models. Follow these steps to install Ollama:

1. Download Ollama from the official website:  
   [https://ollama.com](https://ollama.com)

2. Install Ollama following the provided instructions for your operating system.

### 3. Download Models

To use models such as **Llama 3B** and **DeepSeek**, download them by running the following commands in your command prompt or terminal:

- Download **Llama 3B**:
  ```bash
  ollama run llama3:latest
  ```

- Download **DeepSeek**:
  ```bash
  ollama run deepseek-r1:1.5b
  ```

### 4. Start Ollama

Once the models are downloaded, open a command prompt or terminal and start Ollama with the following command:

```bash
ollama start
```

This will start the Ollama service and make the models ready for interaction.

### 5. Execute the `main.py` Script

Now, you can run the main Python script of the project by executing the following command:

```bash
python main.py
```
## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License - see the [LICENSE](LICENSE) file for details.


The script will interact with the models you downloaded, allowing you to perform specific tasks defined in the `main.py`.

## Additional Notes

- Ensure that Ollama is properly running before executing the Python script.
- If you encounter any errors during the installation or execution, check the [Ollama Documentation](https://ollama.com/docs) for troubleshooting tips.

---

