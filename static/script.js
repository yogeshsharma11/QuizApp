document.addEventListener("DOMContentLoaded", function () {
    const userNameInput = document.getElementById("userName");
    const nameError = document.getElementById("nameError");
    const startQuizBtn = document.getElementById("startQuizBtn");
    const quizList = document.getElementById("quizList");
    const quizQuestionsDiv = document.getElementById("quizQuestions");
    const questionsListDiv = document.getElementById("questionsList");
    const submitQuizBtn = document.getElementById("submitQuizBtn");
    const scoreSection = document.getElementById("scoreSection");
    const scoreText = document.getElementById("scoreText");
    const retryQuizBtn = document.getElementById('retryQuizBtn');

    let quizData = {}; 

    startQuizBtn.addEventListener("click", function () {
        const userName = userNameInput.value.trim();
        if (!userName) {
            nameError.classList.remove("hidden");
        } else {
            nameError.classList.add("hidden");
            quizList.classList.toggle("hidden");
            if (!quizList.classList.contains("hidden")) {
                setTimeout(() => {
                    quizList.classList.add("opacity-100");
                }, 10);
            } else {
                quizList.classList.remove("opacity-100");
            }
        }
    });
    quizList.addEventListener("click", function (event) {
        if (event.target.classList.contains("quiz-item")) {
            const quizId = event.target.getAttribute("data-quiz-id");
            fetchQuizQuestions(quizId);
        }
    });

    
    function fetchQuizQuestions(quizId) {
        fetch(`/quiz_questions/${quizId}`)
            .then(response => response.json())
            .then(data => {
                quizData = data; 

                questionsListDiv.innerHTML = ''; 

    
                data.questions.forEach((question, index) => {
                    const questionDiv = document.createElement("div");
                    questionDiv.classList.add("mb-4");
                    questionDiv.innerHTML = `
                        <p class="text-gray-100">${index + 1}. ${question.question_text}</p>
                        <div>
                            <label>
                                <input type="radio" name="question-${question.id}" value="a" /> ${question.a}
                            </label>
                        </div>
                        <div>
                            <label>
                                <input type="radio" name="question-${question.id}" value="b" /> ${question.b}
                            </label>
                        </div>
                        <div>
                            <label>
                                <input type="radio" name="question-${question.id}" value="c" /> ${question.c}
                            </label>
                        </div>
                        <div>
                            <label>
                                <input type="radio" name="question-${question.id}" value="d" /> ${question.d}
                            </label>
                        </div>
                    `;
                    questionsListDiv.appendChild(questionDiv);
                });

                quizQuestionsDiv.classList.remove("hidden");
            })
            .catch(error => console.error("Error fetching quiz questions:", error));
    }

    submitQuizBtn.addEventListener("click", function () {
        if (!quizData || !quizData.questions || quizData.questions.length === 0) {
            console.error('No quiz data available or no questions fetched');
            return;
        }

        let score = 0;
        const totalQuestions = quizData.questions.length;

        quizData.questions.forEach((question) => {
            const selectedOption = document.querySelector(`input[name="question-${question.id}"]:checked`);
            if (selectedOption && selectedOption.value === question.correct_option) {
                score++;
            }
        })
        scoreText.textContent = `${score}/${totalQuestions} Correct`;
        scoreSection.classList.remove("hidden");
    });
    retryQuizBtn.addEventListener('click', function () {
        
        document.querySelectorAll('input[type="radio"]:checked').forEach(radio => radio.checked = false);
        scoreSection.classList.add('hidden'); 
        quizQuestionsDiv.classList.add('hidden'); 
        quizList.classList.remove('hidden'); 
    });
});
