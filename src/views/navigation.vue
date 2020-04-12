<template>
  <v-navigation-drawer v-model="drawer" temporary absolute>
    <v-list-item two-line>
      <v-list-item-content>
        <v-list-item-title
          style="text-align:center;font-size:20px;display:inline-block;"
          >格式设置</v-list-item-title
        >
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>

    <v-list>
      <v-menu offset-x>
        <template v-slot:activator="{ on }">
          <v-list-item link v-on="on">
            <v-list-item-icon>
              <v-icon>mdi-format-paint</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>主题</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
        <v-list>
          <v-list-item
            v-for="color in colors"
            :key="color"
            :class="color"
            link
            @click.native="appTheme(color)"
          ></v-list-item>
        </v-list>
      </v-menu>

      <v-list-item link @click.native="uploadImg">
        <v-list-item-icon>
          <v-icon>mdi-image</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>背景图片</v-list-item-title>
          <input
            ref="changeImg"
            type="file"
            name=""
            id=""
            style="display:none;"
            @change="changeImg"
          />
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data: () => ({
    colors: ["blue", "green", "purple", "red"],
    fonts: [11, 12, 14, 16, 18, 20],
    listShow: null,
    theme: ""
  }),
  computed: {
    drawer: {
      get() {
        return this.$store.state.drawer;
      },
      set(val) {
        this.$store.state.drawer = val;
      }
    }
  },
  methods: {
    appTheme(val) {
      this.$store.state.theme = val;
    },
    changeFont(val) {
      this.$store.state.fontSize = val;
    },
    uploadImg() {
      let uploadBtn = this.$refs.changeImg;
      uploadBtn.click();
    },
    changeImg(e) {
      let config = { headers: { "Content-Type": "multipart/form-data" } };
      let file = e.target.files[0];
      var formData = new FormData();
      formData.append('file',file);
      this.$http.post("/uploadImg", formData, config).then(res => {
        console.log(res);
      }).catch(err => {
        throw err;
      })
    }
  }
};
</script>

<style scoped></style>
