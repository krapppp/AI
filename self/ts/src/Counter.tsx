import React, { useState } from 'react';

const Counter: React.FC = () => {
  const [count, setCount] = useState<number>(0);

  const handleIncrement = (): void => {
    setCount(prev => prev + 1);
  };

  const handleDecrement = (): void => {
    setCount(prev => prev - 1);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Simple Counter</h1>
      <p>Current Count: {count}</p>
      <button onClick={handleIncrement}>+</button>
      <button onClick={handleDecrement} style={{ marginLeft: '10px' }}>-</button>
    </div>
  );
};

export default Counter;
