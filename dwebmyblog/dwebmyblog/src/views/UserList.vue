<template>
  <div id="userlist">
    <div v-for="item in imglist" v-bind:key="item.pk" class="user">
      <img :src="apiurl+'upload/'+item.headImg" alt />
      <p>{{ item.nickName }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      apiurl:'http://127.0.0.1:9000/',
      imglist: [],
      menuId:3
    };
  },
  //用户在看到界面之前，最后vue提供的一次函数执行
  mounted() {
    this.getUserList(this.menuId)
  },
  watch: {
    $route(to){
      console.log(to.query.menuId)
      this.menuId = to.query.menuId
      this.getUserList(this.menuId)
    }
  },    
  methods: {
    getUserList(id){
      console.log('开始获取分类'+id)
      axios({
        url:'http://127.0.0.1:9000/get-user-list/',
        type:'json',
        params:{
          id:id
        },
        method:'get'
      }).then((res)=>{
        console.log(res)
        this.imglist = res.data
      })
    }
  },
};
</script>

<style>
</style>