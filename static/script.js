async function askGoggins() {
    const question = document.getElementById('question').value;
    const responseDiv = document.getElementById('response');
    
    if (question) {
        const response = await fetch('/api/askGoggins', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: question }),
        });
        const data = await response.json();
        responseDiv.textContent = `You: ${question}\nGoggins: ${data.response}\n`;
        document.getElementById('question').value = '';
    }
}
