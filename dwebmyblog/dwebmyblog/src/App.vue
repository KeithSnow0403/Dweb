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
          <div class="item" style="background: #777; color: #fff;">
            <router-link to="/" style="color:#fff;">Django</router-link>
          </div>
          <div class="item">
            <router-link to="/Vuecli">VueCli</router-link>
          </div>
          <div class="item">
            <a>实战博客</a>
          </div>
          <div class="item">
            <a>项目部署</a>
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
export default {};
</script>

<style>
</style>
