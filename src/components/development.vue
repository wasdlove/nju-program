<template>
  <div class="development" style="margin:0 20px;">
    <div style="font-size:20px;font-weight:bold;text-align:center;">近几年厦门外国语学校毕业生情况</div>
    <div style="margin:20px 0;">一：2015-2018年毕业生去向统计</div>
    <table style="width:100%;text-align:center;">
      <tr>
        <th cols="2">年份</th>
        <th cols="2">升学</th>
        <th cols="2">出国</th>
        <th cols="2">就业</th>
      </tr>
      <tr>
        <td>2018</td>
        <td>1</td>
        <td>1</td>
        <td>5</td>
      </tr>
    </table>

    <div id="dvlChart"></div>
    <div style="margin:20px 0;">二：毕业生发展状况典型</div>
    <table style="width:100%;text-align:center;">
      <tr>
        <th cols="2">姓名</th>
        <th cols="2">年级</th>
        <th cols="2">毕业学院</th>
        <th cols="2">发展去向</th>
      </tr>
      <tr>
        <td>戴文谦</td>
        <td>14级</td>
        <td>电子科学与工程学院</td>
        <td>加州大学圣地亚哥分校</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  mounted() {
    let echarts = require("echarts");
    let chart = echarts.init(document.getElementById("dvlChart"));
    chart.setOption({
      title: {
        text: "2015-2018年毕业生去向统计"
      },
      tooltip: {
        trigger: "item"
      },
      series: [
        {
          type: "pie",
          radius: "75%",
          center: ["50%", "50%"],
          data: [
            { value: 0.5, name: "就业" },
            { value: 0.312, name: "升学" },
            { value: 0.125, name: "出国" }
          ]
        }
      ]
    });
  }
};
</script>

<style scoped>
table {
  border-collapse: collapse;
}
table,
td,
th {
  border: 1px solid black;
}
td,
th {
  height: 50px;
}
#dvlChart {
  height: 450px;
  width: 100%;
}
</style>