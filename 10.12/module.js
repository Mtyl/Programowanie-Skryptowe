exports.Operation = class {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  sum() {
    return this.x + this.y;
  }
};
