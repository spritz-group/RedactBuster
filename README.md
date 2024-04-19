<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Mhackiori/RedactBuster">
    <img src="https://i.postimg.cc/qq2hX7xt/Redact-Buster.png" alt="Logo" width="150" height="150">
  </a>

  <h1 align="center">RedactBuster</h1>

  <p align="center">
     Entity Type Recognition from Redacted Documents
    <br />
    <a href="https://github.com/Mhackiori/RedactBuster"><strong>Paper in progress »</strong></a>
    <br />
    <br />
    <a href="">Anonymous Authors</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary><strong>Table of Contents</strong></summary>
  <ol>
    <li>
      <a href="#abstract">Abstract</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
    </li>
    <li>
  </ol>
</details>

<div id="abstract"></div>

## 🧩 Abstract

>The widespread exchange of digital documents in various domains has resulted in abundant private information being shared. This proliferation necessitates redaction techniques to protect sensitive content and user privacy. While numerous redaction methods exist, their effectiveness varies, with some proving more robust than others. As such, the literature proposes several deanonymization techniques, raising awareness of potential privacy threats. However, while none of these methods are successful against the most effective redaction techniques, these attacks only focus on the anonymized tokens and ignore the sentence context. In this paper, we propose **RedactBuster**, the first deanonymization model using sentence context to perform Named Entity Recognition on reacted text. Our methodology leverages fine-tuned state-of-the-art Transformers and Deep Learning models to determine the anonymized entity types in a document. We test RedactBuster against the most effective redaction technique and evaluate it using the publicly available Text Anonymization Benchmark (TAB). Our results show accuracy values up to 0.985 regardless of the document nature or entity type. In raising awareness of this privacy issue, we propose a countermeasure we call **character evasion** that helps strengthen the secrecy of sensitive information. Furthermore, we make our model and testbed open-source to aid researchers and practitioners in evaluating the resilience of novel redaction techniques and enhancing document privacy.

<p align="right"><a href="#top">(back to top)</a></p>
<div id="usage"></div>

## ⚙️ Usage

To execute the attack and testing our countermeasure, start by cloning the repository:

```bash
git clone https://github.com/Mhackiori/RedactBuster.git
cd RedactBuster
```
<sup>NOTE: if you're accessing this data from the anonymized repository, the above command might not work. The dataset should be downloaded [here](https://figshare.com/s/594107d662643b21dbf2) and unzipped in the dataset directory.</sup>

Then, install the required Python packages by running:

```bash
pip install -r requirements.txt
```

While you can add the original ECHR dataset and process it through our scripts, you can also find the processed dataset in the zip file in the [dataset](https://github.com/Mhackiori/RedactBuster/tree/main/dataset) folder.

<p align="right"><a href="#top">(back to top)</a></p>
