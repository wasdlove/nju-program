<template>
  <div class="congratulation">
    <header>
      <div class="title">
        招生喜报
      </div>
    </header>
    <main>
      <div class="select">
        <div class="province">
          <v-autocomplete
            :loading="items[0].loading"
            label="请选择省份"
            :items="items[0].select"
            v-model="province"
            @blur="selectPro"
          ></v-autocomplete>
        </div>
        <div class="schoolName">
          <v-autocomplete
            :loading="items[1].loading"
            label="请选择学校"
            :items="items[1].select"
            v-model="school"
          ></v-autocomplete>
        </div>
      </div>
      <div class="bc_image">
        <div class="bc_image_header">视图</div>
        <div class="image">
          <img :src="imgUrl" alt="" />
          <div class="stuList" :style="styles">
            <div class="table_header">学校名称</div>
            <table>
              <tr>
                <th>姓名</th>
                <th>科类</th>
                <th>投档分数</th>
                <th>录取专业</th>
                <th>录取方式</th>
              </tr>
              <tr>
                <td>1</td>
                <td>2</td>
                <td>3</td>
                <td>4</td>
                <td>5</td>
              </tr>
            </table>
          </div>
        </div>
      </div>
      <div class="change_img">
        <div class="change_img_header">视图调整</div>
        <div class="input_img">
          <div>
            <div class="label">距离顶部：</div>
            <div class="input_content">
              <v-text-field
                label="请输入百分数"
                v-model="inputStyles.top"
              ></v-text-field>
            </div>
          </div>
          <div>
            <div class="label">宽度：</div>
            <div class="input_content">
              <v-text-field
                label="请输入百分数"
                v-model="inputStyles.width"
              ></v-text-field>
            </div>
          </div>
          <div>
            <v-btn text="" color="#650962" @click="showChange">预览</v-btn>
            <v-btn text="" color="#650962" @click="imageSubmit">上传图片</v-btn>
            <input
              type="file"
              name=""
              id=""
              ref="image_input"
              @change="imageChange"
            />
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  data: () => ({
    items: [
      {
        label: "省份",
        select: [
          "贵州省",
          "江苏省",
          "湖南省",
          "重庆市",
          "北京市",
          "上海市",
          "广东省"
        ],
        loading: false
      },
      {
        label: "学校名称",
        select: [],
        loading: false
      }
    ],
    school: "",
    province: "",
    drawer: null,
    tableHead: [],
    studentsInfo: [],
    imgUrl: require("C:/Users/ASUS/Desktop/luquxibao.jpg"),
    tableShow: false,
    styles: {
      color: "gold",
      top: "50%",
      width: "80%"
    },
    inputStyles: {
      top: "",
      width: "1%"
    }
  }),
  mounted() {
    this.getTableValue();
  },
  methods: {
    showChange() {
      for (let key in this.inputStyles) {
        this.styles[key] = this.inputStyles[key];
      }
      console.log(this.styles);
    },
    imageSubmit() {
      this.$refs.image_input.click();
    },
    imageChange(){
      let imageUrl = this.$refs.image_input;
      let file = imageUrl.files[0];
      let form_data = new FormData();
      form_data.append('file',file);
      console.log(form_data.get('file'))
    },
    getTableValue() {
      let stuList = document.querySelector(".stuList");
      let stuListTop = stuList.style.top;
      let stuListWidth = stuList.style.width;
      console.log(stuListWidth);
      this.inputStyles.top = stuListTop;
      this.inputStyles.width = stuListWidth;
    },
    selectPro() {
      this.items[1].select = [];
      this.$http
        .post("/getSchool", {
          data: {
            province: this.province
          }
        })
        .then(res => {
          this.items[1].loading = true;
          setTimeout(() => {
            this.items[1].select.push(...res.data);
            this.items[1].loading = false;
          }, 1000);
        })
        .catch(err => {
          throw err;
        });
    },
    navigationShow() {
      this.$store.state.drawer = !this.$store.state.drawer;
    },
    getInfo() {
      this.studentsInfo = [];
      this.$http
        .post("/getStuInfo", {
          data: {
            school: this.school
          }
        })
        .then(res => {
          this.tableHead = res.data.thead;
          this.studentsInfo = res.data.tbody;
          console.log(res.data);
        })
        .catch(err => {
          throw err;
        });
    },
    toPdf() {
      this.$http
        .post("/luquxibao", {
          school: this.school
        })
        .then(() => {
          console.log("成功");
        })
        .catch(err => {
          throw err;
        });
    }
  }
};
</script>

<style scoped>
@import url("../style/common_congra.css");
</style>
