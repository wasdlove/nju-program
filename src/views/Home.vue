<template>
  <div class="home">
    <v-app-bar color="purple" dark>
      <v-toolbar-title>{{ toolbarTitle }}</v-toolbar-title>

      <v-col cols="3"></v-col>

      <v-col cols="4">
        <v-text-field
          prepend-inner-icon="mdi-magnify"
          label="学校查询"
          hide-details
          v-model="searchSchool"
          @keyup.enter="search"
        ></v-text-field>
      </v-col>
    </v-app-bar>

    <v-content>
      <v-container fluid>
        <v-row>
          <v-col cols="11" style="padding-top:0;background-color:white;">
            <v-tabs align-with-title color="purple" v-if="tabShow">
              <v-tab v-for="item in items" :key="item.title">{{ item.title }}</v-tab>
              <v-tab-item style="margin-top:5px;">
                <rescent></rescent>
              </v-tab-item>
              <v-tab-item style="margin-top:5px;">
                <scholarship></scholarship>
              </v-tab-item>
              <v-tab-item style="margin-top:5px;">
                <development></development>
              </v-tab-item>
            </v-tabs>
            <div v-else id="pdfPart">
              <rescent></rescent>
              <scholarship></scholarship>
              <development></development>
            </div>
          </v-col>
          <v-col cols="1">
            <v-btn color="purple" dark style="top:15px;width:90px;" @click.native="tabChange">打印预览</v-btn>
            <v-btn
              color="purple"
              style="top:30px;width:90px;color:white;"
              @click.native="htmlToPdf"
              :disabled="btnDisable"
            >打印</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </div>
</template>

<script>
// @ is an alias to /src
import items from "../js/item.js";
import rescent from "../components/rescent";
import scholarship from "../components/scholarship";
import development from "../components/development";
import { toPdf } from "../js/toPdf";

export default {
  name: "home",
  components: { rescent, scholarship, development },
  data: () => ({
    searchSchool: "",
    items: items,
    toolbarTitle: "生源质量报告",
    tabShow: true,
    btnDisable: true
  }),
  methods: {
    headerTitle(val) {
      this.toolbarTitle = val;
      this.drawer = false;
    },
    search(){
      this.$refs.rescent.schoolSearch();
    },
    tabChange() {
      this.tabShow = false;
      this.btnDisable = false;
    },
    async htmlToPdf() {
      await this.tabChange();
      let divELe = document.getElementById("pdfPart");
      toPdf(divELe);
    }
  }
};
</script>

<style scoped>
</style>
