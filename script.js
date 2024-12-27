document.addEventListener('DOMContentLoaded', () => {
    const submitBtn = document.getElementById('submitBtn');
    const userInput = document.getElementById('userInput');
    const responseDiv = document.getElementById('response');
    const loadingDiv = document.getElementById('loading');

    submitBtn.addEventListener('click', async () => {
        const text = userInput.value.trim();
        if (!text) return;

        try {
            loadingDiv.style.display = 'block';
            responseDiv.textContent = '';
            
            const response = await fetch('http://127.0.0.1:5000/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            responseDiv.textContent = data.response;
        } catch (error) {
            responseDiv.textContent = 'אירעה שגיאה בעיבוד הבקשה. נסה שוב מאוחר יותר.';
            console.error('Error:', error);
        } finally {
            loadingDiv.style.display = 'none';
        }
    });
});
