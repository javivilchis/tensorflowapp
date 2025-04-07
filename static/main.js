document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chatForm");
    const chatBox = document.getElementById("chatBox");
    const userInput = document.getElementById("userInput");
  
    chatForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const message = userInput.value.trim();
      if (!message) return;
  
      appendMessage("user", message);
      userInput.value = "";
  
      const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });
  
      const data = await response.json();
      appendMessage("ai", data.response);
    });
  
    function appendMessage(role, content) {
      const bubble = document.createElement("div");
      bubble.classList.add("chat-bubble", role === "user" ? "user" : "ai");
  
      if (role === "ai") {
        const copyBtn = document.createElement("button");
        copyBtn.className = "btn btn-sm btn-outline-secondary float-end ms-2";
        copyBtn.innerText = "📋";
        copyBtn.title = "Copy";
        copyBtn.onclick = () => {
          navigator.clipboard.writeText(content).then(() => {
            copyBtn.innerText = "✅";
            setTimeout(() => (copyBtn.innerText = "📋"), 1500);
          });
        };
  
        const codeMatch = content.match(/```([\s\S]*?)```/); // Check if the response contains code block (```)
        if (codeMatch) {
          const codeBlock = document.createElement("pre");
          const code = document.createElement("code");
          code.textContent = codeMatch[1].trim();
          codeBlock.appendChild(code);
          bubble.appendChild(codeBlock);
  
          const runBtn = document.createElement("button");
          runBtn.className = "btn btn-sm btn-outline-success mt-2";
          runBtn.innerText = "Run Code";
          runBtn.onclick = () => executeCode(codeMatch[1].trim());
          bubble.appendChild(copyBtn);
          bubble.appendChild(runBtn);
        } else {
          const textSpan = document.createElement("span");
          textSpan.innerText = content;
          bubble.appendChild(copyBtn);
          bubble.appendChild(textSpan);
        }
      } else {
        bubble.innerText = content;
      }
  
      chatBox.appendChild(bubble);
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  
    // Function to execute JavaScript code (You can extend this for Python execution as well on the backend)
    function executeCode(code) {
      try {
        eval(code); // Warning: only use eval safely, and avoid in production environments due to security concerns.
      } catch (err) {
        alert("Error running code: " + err.message);
      }
    }
  });