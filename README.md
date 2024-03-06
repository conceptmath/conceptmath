<div align= "center">
    <h1> ConceptMath </h1>
</div>

<p align="center">  
A Bilingual Concept-wise Benchmark for Measuring Mathematical Reasoning of Large Language Models
</p>

<p align="center">  
📃 <a href="https://arxiv.org/pdf/2402.14660.pdf" target="_blank">Paper</a> • 
🤗 <a href="https://huggingface.co/conceptmath" target="_blank">Data (WIP)</a> • 
🏆 <a href="https://huggingface.co/conceptmath" target="_blank">Leaderboard (WIP)</a>
</p>

## Todo

- [x] Release the research paper.
- [ ] Release the answers of various LLMs on our Conceptmath questions.
- [ ] Release the evaluation code.
- [ ] Release the dataset.
- [ ] Develop and launch an online leaderboard.

      

## 💥What's New
- **[2024.02.22]** Our paper is now accessible at https://arxiv.org/abs/2402.14660.

## About ConceptMath

- ConceptMath is a bilingual (English and Chinese), fine-grained benchmark that evaluates concept-wise mathematical reasoning of Large Language Models (LLMs). Unlike traditional benchmarks that evaluate general mathematical reasoning with an average accuracy, ConceptMath systematically organizes math problems under a hierarchy of math concepts, so that mathematical reasoning can be evaluated at different granularity with conceptwise accuracies. 
<p align="center">
    <img src="assets/fig3-1.png" width="93%"> <br>
    <img src="assets/fig3-2.png" width="93%"> <br>
  <b>ConceptMath</b> comprises a total of <b>4011 math</b> problems across <b>214</b> math concepts.
</p>

- Based on our ConcepthMath, we evaluate a broad range of LLMs, and we observe existing LLMs, though achieving high average accuracies on traditional benchmarks, exhibit significant performance variations across different math concepts and may even fail catastrophically on the most basic ones. 
<p align="center">
    <img src="assets/table1.png" width="93%"> <br>
  Results of different models on our constructed ConceptMath benchmark dataset</b>.
</p>
<p align="center">
    <img src="assets/table2.png" width="47.3%"> 
    <img src="assets/fig2.png" width="45%"> <br>
  (a) Concept accuracies on Middle-EN &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp(b) Mean concept accuracies on Middle-EN.
</p>

- Besides, we also introduce an efficient fine-tuning strategy to enhance the weaknesses of existing LLMs.
<p align="center">
    <img src="assets/fig1.png" width="50%">
    <img src="assets/table3.png" width="43.2%"> <br>
  <b>Left</b>: The concept-wise accuracies of LLaMA2-13B and the fine-tuned version based on our efficient finetuning method (i.e., LLaMA2-FT); <b>Right</b>: Introducing CS data specifically for the bottom 10 concepts significantly enhances these concepts’ performance, while slightly improving the performance across the remaining 33 concepts.
</p>



## Cite
Feel free to cite us if you like ConceptMath.

```bibtex
@article{concepthmath,
  title={ConceptMath: A Bilingual Concept-wise Benchmark for Measuring Mathematical Reasoning of Large Language Models},
  author={Yanan Wu and Jie Liu and Xingyuan Bu and Jiaheng Liu and Zhanhui Zhou and Yuanxing Zhang and Chenchen Zhang and Zhiqi Bai and  Haibin Chen and Tiezheng Ge and  Wanli Ouyang and Wenbo Su and Bo Zheng},
  journal={arXiv},
  year={2024}
}
```