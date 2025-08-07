# 🔬 GC Content Analysis of a Genome

## 🧩 Objective
To calculate and visualize the GC content across a genome using a sliding window approach, and identify GC-rich and GC-poor regions.

---

## 📁 Input
A FASTA file containing a complete genome, chromosome, or DNA sequence.

### Example:
- Organism: *Escherichia coli* (E. coli)
- Source: [NCBI Genome Database](https://www.ncbi.nlm.nih.gov/genome/)

---

## 🔧 Tools & Technologies
- **Python 3.x**
- **Biopython** for FASTA parsing
- **Matplotlib** for visualization
- **CSV** for output

---

## 📜 Features
- Reads a genome FASTA file
- Uses a sliding window to calculate GC content per region
- Outputs GC content at each window to a CSV file
- Visualizes GC content across the genome using a line plot

---

## 🚀 How to Run

### 1. Clone this Repository
```bash
git clone https://github.com/yourusername/gc-content-analysis.git
cd gc-content-analysis
