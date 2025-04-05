const express = require("express");
const { Configuration, OpenAIApi } = require("openai");
const dotenv = require("dotenv");
const cors = require("cors");

dotenv.config();
console.log("✅ server.js 有被執行");
console.log("🔑 API Key 是：", process.env.OPENAI_API_KEY);

const app = express();
app.use(cors());
app.use(express.json());

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

app.post("/recommend", async (req, res) => {
  const { userInput } = req.body;

  try {
    const gptResponse = await openai.createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "system",
          content: "你是一個親切的課程推薦助理，根據使用者的興趣提供相關課程建議。",
        },
        {
          role: "user",
          content: userInput,
        },
      ],
    });

    const reply = gptResponse.data.choices[0].message.content;
    res.json({ reply });
  } catch (error) {
    console.error("❌ GPT 錯誤：", error.message);
    res.status(500).json({ error: "GPT API 錯誤" });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`🚀 GPT server 已啟動：http://localhost:${PORT}`);
});
