<template>
  <div id="home">
    <div>
      <div class="header">
        <h1>title</h1>
        <img src="./assets/admin.jpg" alt />
      </div>

      <hr />

      <div class="content">
        <div class="menu">
          <div v-for="item in menuList" :key="item.id" class="item">
            <div 
              v-if="item.id==choosed" 
              style="background: #777; color: #fff;"
              @click="chooseMenu(item.id)"
            >
              <router-link to="/" style="color:#fff;">{{item.text}}</router-link>
            </div>

            <div 
              v-else 
              style="color: #000;" 
              @click="chooseMenu(item.id)"
            >
              <router-link to="/" style="color:#000;">{{item.text}}</router-link>
            </div>
          </div>
        </div>

        <div class="userlist">
          <p>Django</p>
          <hr />

          <!-- 对应router文件下的index.js -->
          <router-view />
        </div>
      </div>
    </div>

    <hr />

    <div class="foot">Copyright © 2020 KeithSnow</div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      menuList: [],
      choosed: 3,
    };
  },
  mounted() {
    this.getMenuList();
  },
  methods: {
    //获取分类列表
    getMenuList() {
      console.log("开始获取分类");
      axios({
        url: "http://127.0.0.1:9000/get-menu-list/",
        type: "json",
        method: "get",
      }).then((res) => {
        console.log(res);
        this.menuList = res.data;
      });
    },
    chooseMenu(id){
      console.log(id)
      this.choosed = id
    }
  },
};
</script>

<style>
</style>
