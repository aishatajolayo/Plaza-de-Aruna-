document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('revenueChart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [
                'Jan','Feb','Mar','Apr','May','Jun',
                'Jul','Aug','Sep','Oct','Nov','Dec'
            ],
            datasets: [{
                label: 'Revenue',
                data: [12000, 15000, 18000, 14000, 20000, 22000, 25000, 23000, 21000, 26000, 28000, 30000],
                fill: false,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { stepSize: 20000 }
                }
            }
        }
    });
});