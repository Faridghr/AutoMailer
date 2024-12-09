import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class CSVHandler:
    def __init__(self, parent):
        self.parent = parent
        self.csv_data = None

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self.parent, "Select CSV File", "", "CSV Files (*.csv)")
        if not file_path:
            return

        try:
            self.csv_data = pd.read_csv(file_path)
            self.parent.csv_label.setText(f"Loaded: {file_path}")
            columns = "\n".join([f"{{{col}}}" for col in self.csv_data.columns])
            self.parent.columns_text.setText(columns)
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to load CSV: {e}")
