import { useState } from "react";

function Button() {
  const clickCount = useState(0);

    const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <button onClick={handleClick} style={{ padding: '10px 20px', cursor: 'pointer' }}>
      Kliknięto {count}
    </button>
  );
}

export default Button;