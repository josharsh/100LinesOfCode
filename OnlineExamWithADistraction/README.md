# Exam with Video Background

This is a single-page HTML application that presents a quiz over a full-screen YouTube video background. The video plays automatically without user controls, and exam questions (loaded from a JSON file) are displayed in a centered overlay. At the end of the quiz, the application shows the final score along with a review of any questions answered incorrectly.

## Features

- **Full-Screen YouTube Background:**  
  The background video is embedded via an `<iframe>` that covers the entire viewport, using autoplay, mute, loop, and minimal branding.

- **Centered Exam Overlay:**  
  The quiz overlay is centered on the screen with a semi-transparent background, ensuring that the video is visible in the background.

- **Dynamic Question Loading:**  
  Questions are fetched from a `questions.json` file with cache busting to ensure updates are loaded correctly.

- **Quiz Logic and Feedback:**  
  Users answer one question at a time. At the end of the quiz, the final score is displayed along with a review of the incorrect answers.

## Files

- **OnlineExamWithDistraction.html:**  
  The main HTML file that contains the full-screen background video, overlay for the quiz, and all JavaScript logic.

- **questions.json:**  
  A JSON file containing the exam questions, choices, and the index of the correct answer.  
  *Example content:*
  ```json
  [
    {
      "question": "What is 2 + 2?",
      "choices": ["3", "4", "5"],
      "answer": 1
    },
    {
      "question": "What is the capital of France?",
      "choices": ["Berlin", "Madrid", "Paris"],
      "answer": 2
    },
    // ... additional questions ...
  ]
