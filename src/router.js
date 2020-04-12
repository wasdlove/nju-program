import Vue from 'vue'
import Router from 'vue-router'

function route(path,filename,baseUrl,name,children,redirect) {
  return{
    path,
    name,
    children,
    redirect,
    component:()=>import(`${baseUrl}/${filename}.vue`)
  }
}

Vue.use(Router)

export default new Router({
  mode:"history",
  routes: [
    {
      path:'/',
      redirect:'/congratulation',
    },
    route('/congratulation','congratulation','./views','congratulation'),
    route('/home','Home','./views','home',[
      route('/home/rescent','rescent','./components','rescent'),
      route('/home/admissionName','admissionName','./components','admissionName'),
      route('/home/scholarship','scholarship','./components','scholarship'),
      route('/home/development','development','./components','development'),
      route('/home/developmentExample','developmentExample','./components','developmentExample')
    ],'/home/rescent')
  ]
})
