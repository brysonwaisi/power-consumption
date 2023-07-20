import "./App.css";
// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./styles/global.scss";
import Home from "./pages/home/Home";
import Footer from "./components/footer/Footer";

function App() {
  return (
    <div className="app">
      <Home />
      <Footer />
    </div>
  );
}

export default App;
