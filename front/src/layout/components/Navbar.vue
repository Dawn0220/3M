<template>
  <div class="navbar" style="font-family: 'Blacker Text'; font-size: 40px; font-weight: bold;">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
             text-color="#274c4a"
             active-text-color="#274c4a" router>
      <hamburger :is-active="sidebar.opened" class="hamburger-container" @toggleClick="toggleSideBar" />
      <el-menu-item index="/home/index">Homepage</el-menu-item>
      <el-submenu index="2">
        <template slot="title">Task</template>
        <el-menu-item index="/task/released_task" style="font-family: 'Blacker Text'; font-weight: bold;">My Release</el-menu-item>
        <el-menu-item index="/task/participated_task" style="font-family: 'Blacker Text'; font-weight: bold;">My Application</el-menu-item>

      </el-submenu>
      <el-menu-item index="/form/index" class="bar">Release</el-menu-item>

        <div class="right-menu">
      <el-dropdown class="avatar-container" trigger="click">
        <div class="avatar-wrapper">
          <img :src="avatar+'?imageView2/1/w/80/h/80'" class="user-avatar">
          <i class="el-icon-caret-bottom" />
        </div>
        <el-dropdown-menu slot="dropdown" class="user-dropdown">
          <router-link to="/homepage/1">
            <el-dropdown-item style="font-family: 'Blacker Text'; font-weight: bold;">
              Home
            </el-dropdown-item>
          </router-link>
          <el-dropdown-item divided @click.native="logout">
            <span style="font-family: 'Blacker Text'; font-weight: bold; display:block;">Log Out</span>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
      <div class="search_all">
        <el-autocomplete style="font-family: 'Blacker Text'; font-weight: bold; display:block;"
        size="small"
        v-model="input"
        :fetch-suggestions="querySearchAsync"
        placeholder="Search for more"
        @select="submitForm"
        class="search"
        ></el-autocomplete>
      </div>

    </el-menu>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Breadcrumb from '@/components/Breadcrumb'
import Hamburger from '@/components/Hamburger'

export default {
  data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        restaurants: [],
        input:'',
        timeout:  null,
        give_data: {"name":'',"address":'',"people":'',"form":'',"web":'',"description1":'',"description2":''},
      };
    },
  components: {
    Breadcrumb,
    Hamburger
  },
  computed: {
    ...mapGetters([
      'sidebar',
      'avatar'
    ]),
    activeIndex(){
        return this.$route.path
      }
  },
  mounted() {
      this.restaurants = this.loadAll();
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('app/toggleSideBar')
    },
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    },
    loadAll() {
        return [
          { "value": "三全鲜食（北新泾店）", "address": "长宁区新渔路144号" },
          { "value": "Hot honey 首尔炸鸡（仙霞路）", "address": "上海市长宁区淞虹路661号" },
          { "value": "新旺角茶餐厅", "address": "上海市普陀区真北路988号创邑金沙谷6号楼113" },
          { "value": "泷千家(天山西路店)", "address": "天山西路438号" },
          { "value": "胖仙女纸杯蛋糕（上海凌空店）", "address": "上海市长宁区金钟路968号1幢18号楼一层商铺18-101" },
          { "value": "贡茶", "address": "上海市长宁区金钟路633号" },
          { "value": "豪大大香鸡排超级奶爸", "address": "上海市嘉定区曹安公路曹安路1685号" },
          { "value": "茶芝兰（奶茶，手抓饼）", "address": "上海市普陀区同普路1435号" },
          { "value": "十二泷町", "address": "上海市北翟路1444弄81号B幢-107" },
          { "value": "星移浓缩咖啡", "address": "上海市嘉定区新郁路817号" },
          { "value": '喜茶', "address": '福田区中康路卓悦汇商场L01楼L1-36号'},
          { "value": '英嘉尼私人影院', "address": '龙岗区布澜路联创科技园二期'},
          { "value": "阿姨奶茶/豪大大", "address": "嘉定区曹安路1611号" },
          { "value": "新麦甜四季甜品炸鸡", "address": "嘉定区曹安公路2383弄55号" },
          { "value": "Monica摩托主题咖啡店", "address": "嘉定区江桥镇曹安公路2409号1F，2383弄62号1F" },
        ];
    },
    querySearchAsync(queryString, cb) {
        var restaurants = this.restaurants;
        var results = queryString ? restaurants.filter(this.createStateFilter(queryString)) : restaurants;

        clearTimeout(this.timeout);
        this.timeout = setTimeout(() => {
          cb(results);
        }, 3000 * Math.random());
      },
      createStateFilter(queryString) {
        return (state) => {
          return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
    a() {
      document.getElementById("b1").style.color = "#cccc00";
    },
    submitForm() {
      this.give_data.name = this.input;
        this.$router.push({
              path: '/employer/1',
              query: { site: this.give_data }
            })
      },
  }
}
</script>

<style lang="scss" scoped>
.el-menu-demo{
  height: 61px;
}
.search_all{
  margin-left: 40%;
}

.search{
  top: 2px;
  position: relative;
  color: #274c4a;
  width: 40%;

}
.bar{
  background-color: #d9e1da;
}

.search_btn{
  top: 14px;
  position: relative;
  background-color: #274c4a;
}
.navbar {
  height: 90px;
  overflow: hidden;
  position: relative;
  background: #fff;

  .hamburger-container {
    line-height: 46px;
    height: 100%;
    float: left;
    cursor: pointer;
    transition: background .3s;
    -webkit-tap-highlight-color:transparent;

    &:hover {
      background: rgba(0, 0, 0, .025)
    }
  }

  .breadcrumb-container {
    float: left;
  }

  .right-menu {
    float: right;
    height: 100%;
    line-height: 50px;

    &:focus {
      outline: none;
    }

    .right-menu-item {
      display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      color: #5a5e66;
      vertical-align: text-bottom;

      &.hover-effect {
        cursor: pointer;
        transition: background .3s;

        &:hover {
          background: rgba(0, 0, 0, .025)
        }
      }
    }

    .avatar-container {
      margin-right: 30px;

      .avatar-wrapper {
        margin-top: 10px;
        position: relative;

        .user-avatar {
          cursor: pointer;
          width: 40px;
          height: 40px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 25px;
          font-size: 12px;
        }
      }
    }
  }
}
</style>
