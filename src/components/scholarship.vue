<template>
  <div class="scholarship" style="margin:0 20px;">
    <div
      style="font-size:20px;font-weight:bold;text-align:center;margin-bottom:10px;"
    >厦门外国语学校学子在南大获奖学金典型</div>
    <table style="width:100%;text-align:center;" v-for="tab in tabs" :key="tab.name">
      <tr>
        <th cols="2">姓名</th>
        <th cols="2">年级</th>
        <th cols="2">院系</th>
        <th cols="2">所获奖学金</th>
        <th cols="2">奖励金额</th>
      </tr>
      <tr v-for="item in tab.content" :key="item.name">
        <td>{{ item.name }}</td>
        <td>{{ item.year }}</td>
        <td>{{ item.major }}</td>
        <td>{{ item.scholarship }}</td>
        <td>{{ item.amount }}</td>
      </tr>
    </table>
    <div>奖学金简介：</div>
  </div>
</template>

<script>
export default {
  data: () => ({
    tabShow: null,
    tabs: [
      {
        name: "苏宁英才全额奖学金",
        content: [
          {
            name: "",
            year: "",
            major: "",
            scholarship: "",
            amount: ""
          }
        ]
      }
    ]
  })
};
</script>

<style scoped>
.scholarship {
  height: 100%;
}
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
</style>