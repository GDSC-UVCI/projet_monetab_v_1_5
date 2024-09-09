const ctx = document.getElementById('genderChart').getContext('2d');
const genderChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Homme', 'Femme'],
        datasets: [{
            data: [window.totalStudentsMale, window.totalStudentsFemale],  // Access variables via window object
            backgroundColor: ['#36A2EB', '#FF6384'],
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: true,
                position: 'right',
            }
        }
    }
});
