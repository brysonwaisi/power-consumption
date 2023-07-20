import "./home.scss";
import AppList from "../../components/appList/AppList";
import Chart from "../../components/chart/Chart";

const Home = () => {
  return (
    <div className="home">
      <div className="box box1">
        <AppList />
      </div>
      <div className="box box7">
        <Chart />
      </div>
      <div className="box box7">
        <Chart />
      </div>
    </div>
  );
};

export default Home;
