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
              <a style="color:#fff;">{{item.text}}</a>
            </div>

            <div 
              v-else 
              style="color: #000;" 
              @click="chooseMenu(item.id)"
            >
              <a style="color:#000;">{{item.text}}</a>
            </div>
          </div>
        </div>

        <div class="userlist">
          <p>{{choosed_text}}</p>
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
      choosed_text:'Django后端'
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
      for (let i = 0; i < this.menuList.length; i++) {
        if (id == this.menuList[i].id){
          this.choosed_text = this.menuList[i].text
        }        
      }
      //进行id传参跳转
      this.$router.push({path:'/',query:{menuId:id}})
    }
  },
};
</script>

<style>
</style>
