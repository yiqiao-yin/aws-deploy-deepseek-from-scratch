### **📌 AWS Lambda & API Gateway Cost Estimation for Bedrock Model Invocation**
Below is a **cost structure template** for running an AWS Lambda function that **invokes an imported Bedrock model** through **API Gateway**.

---

## **🛠️ Cost Components**
The cost will primarily come from the following AWS services:

1. **AWS Lambda**
   - **Compute time per invocation** (billed per millisecond)
   - **Memory usage**
   - **Free tier available (1M requests & 400,000 GB-seconds per month)**

2. **AWS Bedrock (Model Invocation)**
   - **Bedrock charges based on model usage** (tokens processed)
   - **Different models have different pricing**

3. **API Gateway (REST API)**
   - **Requests per million**
   - **Data transfer costs**

4. **S3 Storage** (for storing artifacts)
   - **If downloading frequently, some GET costs may apply**

---

## **📊 Cost Breakdown for 10 Developers Using 100 Requests Per Day**
Assuming:
- Each developer makes **100 API calls per day**.
- **10 developers** use the API.
- Total invocations per month:  
  ```
  10 developers × 100 calls/day × 30 days = 30,000 API calls/month
  ```

---

### **🖥️ AWS Lambda Costs**
#### **Assumptions:**
- **Memory: 512MB (0.5GB)**
- **Execution time per invocation: 1 second (1000ms)**
- **Requests per month: 30,000**
- **Lambda free tier: 1M requests/month and 400,000 GB-seconds/month**

| Metric | Value |
|--------|--------|
| **Execution Time** | 1 sec (1000 ms) |
| **Memory Used** | 512 MB (0.5GB) |
| **GB-Seconds per Invocation** | `0.5GB × 1s = 0.5 GB-sec` |
| **Total GB-Seconds** | `30,000 × 0.5 GB-sec = 15,000 GB-sec` |
| **Lambda Free Tier** | `400,000 GB-sec/month` |
| **Chargeable GB-Seconds** | `0 GB-sec (within free tier)` |
| **Lambda Cost** | **$0 (Free Tier Covered)** |

**✅ AWS Lambda will be free under the free tier for this usage.**

---

### **🛠️ AWS Bedrock Model Invocation Costs**
#### **Assumptions:**
- Using **DeepSeek-R1-Distill-Llama-70B** or similar.
- AWS Bedrock charges per **input tokens + output tokens**.
- Assume **500 input tokens & 500 output tokens per request**.
- **Cost estimate:** `$0.0005 per 1,000 input tokens` and `$0.002 per 1,000 output tokens`.

| Metric | Value |
|--------|--------|
| **Input Tokens per Invocation** | 500 |
| **Output Tokens per Invocation** | 500 |
| **Total Tokens per Invocation** | 1,000 |
| **Cost per 1,000 Input Tokens** | `$0.0005` |
| **Cost per 1,000 Output Tokens** | `$0.002` |
| **Total Cost per Invocation** | `(500 × $0.0005) + (500 × $0.002) = $0.00125` |
| **Total Cost per Month (30,000 Calls)** | `30,000 × $0.00125 = $37.50` |

✅ **AWS Bedrock Cost per Month: ~$37.50**

---

### **🌐 API Gateway Costs**
#### **Assumptions:**
- REST API pricing is **$3.50 per million requests**.
- 30,000 requests per month.

| Metric | Value |
|--------|--------|
| **Total API Requests** | 30,000 |
| **Cost per Million Requests** | `$3.50` |
| **Total Cost** | `(30,000 / 1,000,000) × $3.50 = $0.105` |

✅ **API Gateway Cost per Month: ~$0.11**

---

### **📦 S3 Storage Costs**
- **One-time storage fee for model artifacts** (~70B model)
- **GET requests if frequently accessed**
- Usually **minimal for inference workloads**.

✅ **Negligible cost for normal usage (~$1/month).**

---

## **📌 Total Monthly Cost Estimate**
| Service | Estimated Monthly Cost |
|----------|----------------------|
| **AWS Lambda** | `$0 (Free Tier Covered)` |
| **AWS Bedrock Model Invocation** | `$37.50` |
| **API Gateway** | `$0.11` |
| **S3 Storage** | `$1 (minimal for inference use)` |
| **Total Estimated Cost** | **$38.61 per month** |

---

## **📌 Cost Scalability**
| API Calls per Month | Bedrock Cost | API Gateway Cost | Total Monthly Cost |
|---------------------|-------------|-----------------|--------------------|
| **30,000 (Base Case)** | `$37.50` | `$0.11` | `$38.61` |
| **100,000** | `$125` | `$0.35` | `$126.35` |
| **500,000** | `$625` | `$1.75` | `$626.75` |
| **1,000,000** | `$1,250` | `$3.50` | `$1,253.50` |

---

## **🎯 Key Takeaways**
✅ **AWS Lambda is Free under Free Tier** for this usage.  
✅ **AWS Bedrock is the primary cost driver (~$37.50/month for 30K requests).**  
✅ **API Gateway costs are negligible (~$0.11/month).**  
✅ **Scales linearly based on API usage.**  

---

## **🛠️ How to Optimize Costs**
1. **Reduce Token Usage**  
   - Decrease **max_gen_len** if possible.
   - Use **shorter prompts**.
   
2. **Use Reserved Capacity for Bedrock**  
   - AWS Bedrock offers **reserved throughput pricing** to reduce costs.

3. **Monitor Usage with AWS Cost Explorer**  
   - Set up billing alerts to avoid surprises.

---

### **📌 Final Thought**
💰 **For 10 developers hitting the API 100 times a day, the estimated AWS cost is ~$38.61 per month.**  
**Scaling up increases costs proportionally, with AWS Bedrock being the main cost driver.** 🚀
