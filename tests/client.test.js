const { io } = require("socket.io-client");

describe("recieve data", () => {
  let socket;
  beforeAll(() => {
    socket = io(`http://localhost:5000`);
  });

  afterAll(() => {
    socket.close();
  });

  test("test_string", () => {
    socket.on("test_string", (arg) => {
        expect(arg).toMatch ("world");
    });
    socket.emit("test_string", "Hello");
  });

  test("test_number", () => {
      socket.on("test_number", (arg) => {
          expect(arg).toBe(42);
      });
      socket.emit("test_number", 42);
  });

  test("test_json", () => {
      socket.on("test_json", (arg) => {
          expect(arg).toStrictEqual({ data: [[1,2,3, 2,3,4]], shape: [2, 3], dtype:'int' });
      });
      socket.emit("test_json", {data: [[1,2,3, 2,3,4]], shape: [2, 3], dtype:'int'});
  });

  test("test_array", () => {
    socket.on("test_array", (arg) => {
        expect(arg).toStrictEqual([[[1,2,3], [2,3,4]], [[1,2,3], [2,3,4]]]);
    });
    socket.emit("test_array", [[[1,2,3], [2,3,4]], [[1,2,3], [2,3,4]]])
  });

});