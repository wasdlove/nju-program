import Vue from "vue";
import Vuex from "vuex";
import items from "./js/item.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawer: null,
    theme: "purple",
    fontSize: "16",
    items: items,
    school:''
  },
  mutations: {

  },
  actions: {}
});
