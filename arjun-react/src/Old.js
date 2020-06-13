import List from "./List";
import basketball from "./basketballreact.png";
import baseball from "./baseball.png";
import football from "./Football.png";

const Old = () => {
  const [toggle, setToggle] = useState(true);

  const printStatement = () => {
    setToggle("Arjun!");
    console.log(toggle);
  };

  return (
    <div>
      <div>
        <h1 style={{ textAlign: "center" }}>Arjun</h1>
      </div>
      <List basketball="basketball" football="football" guitar="guitar"></List>
      <button onClick={() => setToggle(!toggle)}>You don't like the picture? Click here!</button>
      {toggle ? <img src={football}></img> : <img src={baseball}></img>}
      <img src={basketball} width={100} height={100}></img>
    </div>
  );
};

export default Old