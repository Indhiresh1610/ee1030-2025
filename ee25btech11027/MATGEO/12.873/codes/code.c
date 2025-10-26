double calculate_inner_product(double vec_a[3], double vec_b[3]) {
    double product = 0.0;
    
    // The inner product is the sum of the products of corresponding components.
    // a.b = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
    for (int i = 0; i < 3; i++) {
        product += vec_a[i] * vec_b[i];
    }
    
    return product;
}
