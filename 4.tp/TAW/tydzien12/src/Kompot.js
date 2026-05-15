import { useState } from "react";

function Kompot() {
  let formData = {
    gra: "",
    platforma: "",
  };

  const [submittedData, setSubmittedData] = useState({
    gra: "",
    platforma: "",
  });

  const handleChange = (e) => {
    formData[e.target.id] = e.target.value
  };

  const handeFormSubtmit = () => {
    setSubmittedData(formData);
  };

  return (
    <>
      <label htmlFor="gra">Gra</label>
      <input
        type="text"
        id="gra"
        
        onChange={handleChange}
      />

      <label htmlFor="platforma">Platforma</label>
      <input
        type="text"
        id="platforma"
       
        onChange={handleChange}
      />

      <button onClick={handeFormSubtmit}>
        Wklej Dane
      </button>

      
        <>
          <h3>Wysłane dane:</h3>

          <p>Gra: {submittedData.gra}</p>
          <p>Platforma: {submittedData.platforma}</p>
        </>
    </>
  );
}

export default Kompot;