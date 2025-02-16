# Understanding Bedrock Service Charges

## Overview
The experiment tested in this .md file imported the DeepSeek model (131 GB) to Amazon Bedrock and noticed that the service charged $17 on the first day and $12 on the second day. The experiment checked CloudWatch and found that this function is invoked 5-10 times a day, with questions in the size of 1-2 sentences and responses averaging 1024 tokens. Since the usage was not high, it is important to analyze how these costs are calculated.

## Possible Cost Factors
Amazon Bedrock charges can include:

1. **Model Hosting Costs**:
   - Bedrock charges **$0.10 per GB per month** for model storage.
   - The **131 GB model** incurs a monthly storage cost of **$13.10**.
   - Some models require dedicated hosting, adding extra fees depending on configuration.
   
2. **Invocation Charges**:
   - Pricing is based on the number of inference requests and tokens processed.
   - Bedrock charges **$0.02 per 1,000 input tokens** and **$0.04 per 1,000 output tokens**.
   - With **225 requests per month** averaging **1024 tokens per response**, this results in:
     - **Input cost: (225 * 1024) / 1000 * $0.02 = $4.60**
     - **Output cost: (225 * 1024) / 1000 * $0.04 = $9.22**
     - **Total invocation cost: $13.82 per month**.

3. **Provisioned Throughput**:
   - If provisioned capacity is enabled, the experiment is charged for reserved resources.
   - Bedrock pricing for provisioned throughput starts at **$10 per hour**, meaning **$240 per day** if always on.
   - If auto-scaling is enabled, costs may fluctuate but could still contribute significantly.
   
4. **Background Processes**:
   - Keeping a model loaded in memory for fast access may cost **$0.05 - $0.10 per minute**.
   - Even low traffic might lead to **several dollars per day** in idle costs.

5. **Data Transfer Costs**:
   - AWS charges **$0.09 per GB for outbound data transfer** beyond free-tier limits.
   - If API calls are made from a different AWS region, data transfer fees could add up.

## Estimated Monthly Cost
Given the current usage pattern:
- **Invocation Rate**: Assuming an average of **7.5 invocations per day**, the monthly total is **225 requests**.
- **Token Consumption**: Each request averages **1024 tokens**, leading to **230,400 tokens per month**.
- **Invocation Cost**: **$13.82 per month**.
- **Hosting Cost**: **$13.10 per month**.
- **Provisioned Throughput Cost (if always on)**: **Up to $7,200 per month** (not applicable for on-demand usage).
- **Idle Compute Cost**: Estimated **$30 - $100 per month**.
- **Data Transfer Cost**: **Variable, depends on cross-region API usage**.
- **Estimated Total Cost (On-Demand Usage Only)**: **$30 - $130 per month**, depending on background usage.

## Cost-Saving Measures
To reduce costs, consider the following:

1. **Switch to On-Demand Inference**:
   - If provisioned throughput is enabled, switching to on-demand can prevent unused capacity charges, reducing potential costs from **$7,200 per month** to **$30 - $130 per month**.

2. **Optimize Invocation Usage**:
   - Use batching to send multiple questions in a single request, reducing API calls by **30-50%**.
   - Implement caching mechanisms to avoid redundant calls.

3. **Reduce Token Consumption**:
   - Limit response size where possible to decrease processing costs by **10-20%**.
   - Adjust model parameters to optimize token usage.

4. **Monitor Auto-scaling and Background Processes**:
   - Ensure that Bedrock is not maintaining an active instance unnecessarily.
   - Setting idle timeouts can save **$30 - $100 per month**.

5. **Review Data Transfer Costs**:
   - Ensure requests and responses remain within the same AWS region to avoid cross-region data transfer fees. Given that the model is **131 GB** and stored in **S3**, each invocation retrieves parts of the model, potentially incurring **S3 data transfer costs**. AWS charges **$0.09 per GB** for outbound S3 data transfer beyond the free tier, meaning that if 10% of the model is accessed per invocation (13.1 GB), the cost could be **$1.18 per invocation**, adding up to **$265 per month** for 225 invocations.
   
By implementing these measures, this experiment can optimize AWS Bedrock usage and reduce monthly expenses significantly.

