document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector('form');
    const subject = document.getElementById('subject');
    const year = document.getElementById('year');
    const question = document.getElementById('question');

    function autoSubmit() {
        if (subject.value && year.value && question.value) {
            form.submit();
        }
    }

    subject.addEventListener('change', autoSubmit);
    year.addEventListener('change', autoSubmit);
    question.addEventListener('change', autoSubmit);
});
