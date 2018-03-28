var a = [
    {
        label:['剩余流量'],
        data:80,
        color:'#1aad19'
    },
    {
        label:'已用流量',
        data:20,
        color:'#999'
    },
];

$.plot($("#donut-chart"), a, {
    series: {
        pie: {
            innerRadius: .5,
            show: !0,
            combine: {
                color: "#999",
                threshold: .1
            }
        }
    },
    grid: {
        borderWidth: 0,
        hoverable: !1,
        clickable: !1
    },
    legend: {
        show: !1
    }
})